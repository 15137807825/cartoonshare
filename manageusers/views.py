from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView, CreateAPIView
# Create your views here.
from rest_framework.response import Response

from user.models import ManageUser
from manageusers.userserializers import ManagerSerializers, ManagerLoginSerializer, ManagerRegisterSerializers
from user.util import token_confirm



#管理员认证
class ManagerShowView(GenericAPIView):

    """
    管理员认证接口
    """

    queryset = ManageUser.objects.all()
    serializer_class = ManagerSerializers

    def get(self,request):
        #获取token
        token = request.query_params.get('token')
        try:
            uid = token_confirm.confirm_validate_token(token)
        except Exception as e:
            print(e)
            return Response({
                'code':107,
                'msg':'token失效，请重新登录',
                'data':{}
            })
        # 获取到了uid
        try:
            user = ManageUser.objects.get(pk=uid)
        except Exception as e:
            print(e)
            return Response({
                'code':107,
                'msg':'该用户不存在',
                'data':{}
            })

        # 序列化
        serializer = ManagerSerializers(instance=user)
        return Response({
            'code':200,
            'msg':'查询成功',
            'data':{
                'user_info':serializer.data
            }
        })

#管理员注册
class ManagerRegisterView(GenericAPIView):

    """
    管理员注册接口
    """

    queryset = ManageUser.objects.all()
    serializer_class = ManagerRegisterSerializers

    def post(self,request):
        #反向序列化
        serializer = self.get_serializer(data=request.data)
        #验证
        if serializer.is_valid():
            # 保存
            user = serializer.save()
            print(user)
            return Response({
                'code':1,
                'msg':'注册成功',
                'data':{'user_id':user.id}
            })
        return Response({
            'code': 0,
            'msg': '注册失败',
            'data':{'info':serializer.errors}
        })

#管理员登陆
class ManagerLoginView(CreateAPIView):

    """
    管理员登录接口
    """

    queryset = ManageUser.objects.all()
    serializer_class =ManagerLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        #验证通过
        if serializer.is_valid():
            #产生token
            username = serializer.data.get('u_username')
            user = ManageUser.objects.filter(u_username=username).first()
            # 生成token
            token = token_confirm.generate_validate_token(user.id)
            print(token)
            return Response({'code': status.HTTP_200_OK,
                             'msg': '登录成功',
                             'data': {'user_id': user.id, 'token': token}})
        else:  # 验证没通过
            print(serializer.errors)
            return Response({'code': 1004,
                             'msg': '校验参数错误',
                             'data': {'error': serializer.errors, 'token': None}})