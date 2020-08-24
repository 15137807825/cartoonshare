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
from django.urls import path

from manageinfo import views

app_name = 'manageinfo'

urlpatterns = [
    #删除动漫
    path('cdelete/<int:pk>/',views.DeleteCartoonView.as_view(),name='cdelete'),
    # 添加动漫
    path('ccreate/', views.CreateCartoonView.as_view(), name='ccreate'),
    #修改动漫
    path('cchange/<int:pk>/', views.ChangeCartoonView.as_view(), name='cchange'),
    # 添加动漫类型
    path('tcreate/', views.CreateCartoonTypeView.as_view(), name='tcreate'),
    #删除动漫类型
    path('tdelete/<int:pk>/', views.DeleteCartoonTypeView.as_view(), name='tdelete'),
    #添加动漫信息
    path('screate/', views.CreateCartoonShowView.as_view(), name='screate'),
    # 修改动漫信息
    path('schange/<int:pk>/', views.ChangeCartoonShowView.as_view(), name='schange'),
    #删除用户
    path('udelete/<int:pk>/', views.DeleteCartoonUserView.as_view(), name='udelete'),
    #修改用户信息
    path('uchange/<int:pk>/', views.ChangeCartoonUserView.as_view(), name='uchange'),




]
