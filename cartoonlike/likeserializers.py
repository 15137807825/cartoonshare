from user.models import Cartoons, Cartoonlike
from rest_framework import serializers


#卡通详细信息序列化器
class CartoonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartoons
        fields = '__all__'


class likeAddSerializer(serializers.Serializer):
    cartoonsid = serializers.CharField(required=True)
    token = serializers.CharField()

    def validate_cartoonsid(self, value):
        value = int(value)
        print(value)
        the_cartoons = Cartoons.objects.filter(pk=value).first()
        #商品不存在就报错
        if not the_cartoons:
            raise serializers.ValidationError("动漫不存在")
        #商品存在就返回value
        return value

    def validate_token(self, data):
        if not data:
            raise serializers.ValidationError("token不存在")
        return data


class LikeSerializer(serializers.ModelSerializer):
    c_goods = CartoonsSerializer()  # 关联序列化
    class Meta:
        model = Cartoonlike
        fields = "__all__"