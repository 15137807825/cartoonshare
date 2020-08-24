
#用于实现进入喜欢的动漫界面的用户许可
from rest_framework.permissions import BasePermission

from user.models import CartoonUser


class UserLikepermission(BasePermission):
    def has_permission(self, request, view):
        # 登录用户返回True,未登录的用户返回False
        return isinstance(request.user,CartoonUser)