from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView, CreateAPIView
# Create your views here.
from rest_framework.response import Response

from user.models import CartoonUser
from user.userserializers import UserSerializers, UserRegisterSerializers, UserLoginSerializer
from user.util import token_confirm



#用户认证
class UserShowView(GenericAPIView):
    """
    用户认证接口
    """
    queryset = CartoonUser.objects.all()
    serializer_class = UserSerializers

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
            user = CartoonUser.objects.get(pk=uid)
        except Exception as e:
            print(e)
            return Response({
                'code':107,
                'msg':'该用户不存在',
                'data':{}
            })

        # 序列化
        serializer = UserSerializers(instance=user)
        return Response({
            'code':200,
            'msg':'查询成功',
            'data':{
                'user_info':serializer.data
            }
        })

#用户注册
class UserRegisterView(GenericAPIView):

    """
    用户注册接口
    """

    queryset = CartoonUser.objects.all()
    serializer_class = UserRegisterSerializers

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


#用户登陆
class UserLoginView(CreateAPIView):

    """
    用户登录接口
    """

    queryset = CartoonUser.objects.all()
    serializer_class =UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        #验证通过
        if serializer.is_valid():
            #产生token
            username = serializer.data.get('u_username')
            user = CartoonUser.objects.filter(u_username=username).first()
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