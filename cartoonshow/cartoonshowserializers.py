from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from user.models import CartoonShow, Cartoontype, Cartoons, Cartoonlike


#卡通序列化器
class CartoonsSerialzer(serializers.ModelSerializer):
    likes = PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Cartoons
        fields = "__all__"
        extra_kwargs = {
            'ctitle': {
                'required': True,
                'help_text': '动漫名'
            }

        }

#卡通类型序列化器
class CartoonTypeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Cartoontype
        fields = '__all__'

#喜欢的卡通序列化器
class CartoonlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartoonlike
        fields = '__all__'