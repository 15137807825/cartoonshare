from django.shortcuts import render

from manageinfo.ManageAuthentications import ManageAuthentication
from manageinfo.ManagePermission import Managerpermission
from manageinfo.Manageserializers import CartoonsSerializer, CartoonTypeSerializer, CartoonShowSerializer, \
    CartoonUserSerializer
from user.models import Cartoons, CartoonShow, Cartoontype, CartoonUser
# Create your views here.
from rest_framework.generics import DestroyAPIView, CreateAPIView,UpdateAPIView


#删除动漫
class DeleteCartoonView(DestroyAPIView):

    """
    删除动漫接口
    """

    queryset = Cartoons
    serializer_class = CartoonsSerializer
    #管理员权限验证(如需测试，请注释下面两行代码)
    # authentication_classes = ManageAuthentication,
    # permission_classes = Managerpermission,



#添加动漫
class CreateCartoonView(CreateAPIView):

    """
    添加动漫接口
    """

    serializer_class = CartoonsSerializer
    # 管理员权限验证(如需测试，请注释下面两行代码)
    # authentication_classes = ManageAuthentication,
    # permission_classes = Managerpermission,

#修改动漫
class ChangeCartoonView(UpdateAPIView):

    """
    修改动漫接口
    """

    queryset = Cartoons
    serializer_class = CartoonsSerializer
    # 管理员权限验证(如需测试，请注释下面两行代码)
    # authentication_classes = ManageAuthentication,
    # permission_classes = Managerpermission,


#添加动漫类型
class CreateCartoonTypeView(CreateAPIView):

    """
    添加动漫类型接口
    """

    queryset = Cartoontype
    serializer_class = CartoonTypeSerializer
    # 管理员权限验证(如需测试，请注释下面两行代码)
    # authentication_classes = ManageAuthentication,
    # permission_classes = Managerpermission,


#删除动漫类型
class DeleteCartoonTypeView(DestroyAPIView):

    """
    删除动漫类型接口
    """

    queryset = Cartoontype
    serializer_class = CartoonTypeSerializer
    # 管理员权限验证(如需测试，请注释下面两行代码)
    # authentication_classes = ManageAuthentication,
    # permission_classes = Managerpermission,

#添加动漫信息
class CreateCartoonShowView(CreateAPIView):

    """
    添加动漫信息接口
    """

    queryset = CartoonShow
    serializer_class = CartoonShowSerializer
    # 管理员权限验证(如需测试，请注释下面两行代码)
    # authentication_classes = ManageAuthentication,
    # permission_classes = Managerpermission,

#修改动漫详细信息
class ChangeCartoonShowView(UpdateAPIView):

    """
    修改动漫信息接口
    """

    queryset = CartoonShow
    serializer_class = CartoonShowSerializer
    # 管理员权限验证(如需测试，请注释下面两行代码)
    # authentication_classes = ManageAuthentication,
    # permission_classes = Managerpermission,

#删除用户信息
class DeleteCartoonUserView(DestroyAPIView):

    """
    删除用户信息接口
    """

    queryset = CartoonUser
    serializer_class = CartoonUserSerializer
    # 管理员权限验证(如需测试，请注释下面两行代码)
    # authentication_classes = ManageAuthentication,
    # permission_classes = Managerpermission,

#修改用户信息
class ChangeCartoonUserView(UpdateAPIView):

    """
    修改用户信息接口
    """

    queryset = CartoonUser
    serializer_class = CartoonUserSerializer
    # 管理员权限验证(如需测试，请注释下面两行代码)
    # authentication_classes = ManageAuthentication,
    # permission_classes = Managerpermission,

