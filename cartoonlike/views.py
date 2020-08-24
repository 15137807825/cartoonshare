
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from cartoonlike.LikePermission import UserLikepermission
from cartoonlike.LikeAuthentications import UserLikeAuthentication
from cartoonlike.likeserializers import LikeSerializer, likeAddSerializer
from user.models import CartoonUser, Cartoonlike, Cartoons

# Create your views here.
from user.util import token_confirm


#添加喜欢的动漫
class LikeAddView(CreateAPIView):

    """
    添加喜欢的动漫接口
    """

    queryset = CartoonUser.objects.all()
    serializer_class = likeAddSerializer
    #用户信息认证
    authentication_classes = UserLikeAuthentication,
    permission_classes = UserLikepermission,

    def create(self, request, *args, **kwargs):
        # 生成序列化器
        serializer = self.get_serializer(data=request.data)
        print("add_like")
        user = request.user
        if not isinstance(user,CartoonUser):
            return Response({'code':105,'msg':'你尚未登录','data':{}})
        if serializer.is_valid():
            #商品存在
            #在like里找到用户的记录
            #跨表查询
            likes = Cartoonlike.objects.filter(c_user=user)
            cartoonsid = serializer.data.get('cartoonsid')
            print(cartoonsid)
            print(list(likes))
            the_like = Cartoons.objects.get(pk=cartoonsid)
            carts = likes.filter(c_cartoons=the_like)
            print(likes)
            # 喜欢的动漫中有该种动漫
            if likes.exists():
                like = likes.first()  #获取该动漫的记录
                like.c_cartoons_num += 1
                like.save()
            else:  # 喜欢的动漫中没有该动漫
                like = Cartoonlike()
                like.c_cartoons_num = 1
                like.c_cartoons = the_like
                like.c_user = user
                like.c_is_select = 1
                like.save()
            return Response({'code':200,'msg':'ok','data':{'c_cartoon_num':like.c_cartoons_num}})
        else:
            Response({'code': 1006, 'msg': '动漫不存在', 'data': {}})

#喜欢的动漫列表
class LikeListView(ListAPIView):
    queryset = Cartoonlike.objects.all()
    serializer_class = LikeSerializer
    #用户信息认证
    authentication_classes = UserLikeAuthentication,
    permission_classes = UserLikepermission,

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        print(request.user)
        # 自己的喜欢动漫的记录
        queryset = queryset.filter(c_user=request.user)
        queryset = self.filter_queryset(queryset)

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'code':200,
            'msg':'查询成功',
            'data':{
                'title':'喜欢的动漫',
                'is_all_select':True,
                'likes':serializer.data
            }
        })
