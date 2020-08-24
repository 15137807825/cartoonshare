"""cartoonshare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    #用户url
    path('cartoon/user/', include('user.urls')),
    #管理员url
    path('cartoon/managers/', include('manageusers.urls')),
    #管理后台信息url
    path('cartoon/manageinfo/', include('manageinfo.urls')),
    #动漫展示界面url
    path('cartoon/show/', include('cartoonshow.urls')),
    #喜欢的动漫url
    path('cartoon/like/', include('cartoonlike.urls')),
    #漫画分享网站接口文档
    path('docs/', include_docs_urls(title='漫画分享网站接口文档'))
]
