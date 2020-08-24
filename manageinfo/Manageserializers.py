from rest_framework import serializers

from user.models import Cartoons,Cartoontype,CartoonShow,CartoonUser

#动漫序列化器
class CartoonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartoons
        fields = '__all__'

#动漫类型序列化器
class CartoonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartoontype
        fields = '__all__'

#动漫详情展示序列化器
class CartoonShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartoonShow
        fields = '__all__'


#用户管理序列化器
class CartoonUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartoonUser
        fields = '__all__'

