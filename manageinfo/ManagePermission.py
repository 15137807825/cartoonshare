from rest_framework.permissions import BasePermission

from user.models import ManageUser


class Managerpermission(BasePermission):
    def has_permission(self, request, view):
        # 登录用户返回True,未登录的用户返回False
        return isinstance(request.user,ManageUser)