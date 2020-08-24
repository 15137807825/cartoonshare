from django_filters import rest_framework as filters

from user.models import CartoonShow, Cartoons

#自定义过滤器
class CartoonFilter(filters.FilterSet):
    class Meta:
        model = Cartoons

        fields ={
            #根据名称查询
            'ctitle': ['icontains','startswith'], #不区分大小写的包含
            #根据作者查询
            'cauth': ['icontains','startswith'],
            #根据日期查询
            'cpub_date':['startswith','endswith'],
            # #根据类型查询
            'ctype_id':['in'],

        }

