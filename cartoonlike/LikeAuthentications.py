
from rest_framework.authentication import BaseAuthentication
from user.models import CartoonUser
from user.util import token_confirm


class UserLikeAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 获取token值
        token = request.data.get('token',None) or request.query_params.get('token',None)
        print(11,token)
        try:
            uid = token_confirm.confirm_validate_token(token)
        except Exception as e:
            return
        try:
            user = CartoonUser.objects.get(pk=uid)
        except Exception as e:
            return
        print(22)
        # 验证成功
        return user, token