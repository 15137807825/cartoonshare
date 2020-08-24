from django.db.models import Count
from django.shortcuts import render
from rest_framework import filters
from rest_framework.generics import ListAPIView, GenericAPIView

# Create your views here.
from rest_framework.response import Response

from cartoonshow.cartoonshowserializers import CartoonsSerialzer,CartoonlikeSerializer
from cartoonshow.myfilters import CartoonFilter
from cartoonshow.MyPaginations import BookListPager
from user.models import Cartoons,Cartoonlike

class CartoonListView(GenericAPIView):

    """
    卡通展示
    """
    queryset = Cartoonlike.objects.all()
    serializer_class = CartoonlikeSerializer
    def get(self,request):
        # #统计cartoonlike表里每个id出现的次数
        res = Cartoonlike.objects.values('c_cartoons_id').annotate(Count('id'))
        #将id按出现的次数由大到小排序
        res = res.order_by('id__count').reverse()
        print(res)
        cartoons_queryset = Cartoons.objects.all()

        filter_backends = filters.OrderingFilter
        #支持排序的字段
        ordering_fields = (Count('likes'))
        cartoons_data = CartoonsSerialzer(cartoons_queryset,many=True)
        return Response({
            'code': 100,
            'msg': '请求成功',
            'data': {
                'main_show': cartoons_data.data,
            }
        })





class CartoonfilterView(ListAPIView):

    """
    卡通过滤器（即查询卡通）
    """

    queryset = Cartoons.objects.all()
    serializer_class = CartoonsSerialzer
    filter_class = CartoonFilter

