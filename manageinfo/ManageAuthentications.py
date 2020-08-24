from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from user.models import ManageUser
from user.util import token_confirm


class ManageAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 获取token值
        token = request.data.get('token',None) or request.query_params.get('token',None)
        print(11,token)
        try:
            uid = token_confirm.confirm_validate_token(token)
        except Exception as e:
            # print(e)
            return
        try:
            user = ManageUser.objects.get(pk=uid)
        except Exception as e:
            # print(e)
            # raise APIException({'code': 1006, 'msg': '用户不存在', 'data': {}})
            return
        print(22)
        # 验证成功
        return user, token