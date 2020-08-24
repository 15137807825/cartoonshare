from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from user.models import CartoonUser




#用户信息序列化器
class UserSerializers(serializers.Serializer):
    class Meta:
        model =CartoonUser
        fields ="__all__"


#用户注册序列化
class UserRegisterSerializers(serializers.Serializer):
    u_username = serializers.CharField(required=True)
    u_password = serializers.CharField(min_length=3,max_length=12,error_messages={'max_length': '最大长度不能大于12个字符',
                                                                                  'min_length': '最小长度不能小于3个字符'
                                                                                  })
    #确认密码
    u_password2 = serializers.CharField(min_length=3,max_length=12,error_messages={
        'max_length':'最大长度不能大于12个字符',
        'min_length':'最小长度不能小于3个字符',

    })
    u_email = serializers.EmailField(required=True)

    #验证用户名是否唯一
    def validate_u_username(self,attrs):
        print(attrs)
        #先获取重名用户名
        user = CartoonUser.objects.filter(u_username=attrs).first()
        #如果重名用户存在
        if user:
            raise serializers.ValidationError('用户名已经存在')
        return attrs

    #全局验证，验证两次输入的密码相等
    def validate(self,attrs):
        password = attrs.get('u_password')
        password2 = attrs.get('u_password2')
        if password != password2:
            raise serializers.ValidationError({'u_password':'两次密码不一致'})
        return attrs
    #保存用户验证后的信息
    def create(self, validated_data):
        user = CartoonUser()
        password = validated_data.get('u_password')
        password = make_password(password)  # 对密码加密
        user.u_username = validated_data.get('u_username')
        user.u_password = password
        user.u_email = validated_data.get('u_email')
        user.is_active = 1  # 活动用户
        user.is_delete = 0  # 未删除
        user.save()
        return user

# 登录序列化
class UserLoginSerializer(serializers.Serializer):
    u_username = serializers.CharField(required=True,min_length=3)
    u_password = serializers.CharField(required=True,min_length=3)

    def validate(self,attrs):
        username = attrs.get('u_username')
        password = attrs.get('u_password')
        #先查询对比有无注册过
        user = CartoonUser.objects.filter(u_username=username)
        #如果不存在
        if not user.exists():
            raise serializers.ValidationError('用户不存在')
        #用户存在
        user = user.first()
        # 成功返回ture，失败返回False，这里只处理失败的，check_password(明文密码，签名密码)
        if not check_password(password,user.u_password):
            raise serializers.ValidationError('用户名或密码错误')
        return attrs

