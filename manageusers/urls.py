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

from manageusers import views

app_name = 'manageusers'

urlpatterns = [
    #管理员信息展示
    path('managers/',views.ManagerShowView.as_view(),name='managers'),
    #管理员注册
    path('managers/register/', views.ManagerRegisterView.as_view(), name='mregister'),
    # 管理员登陆
    path('manager/login/', views.ManagerLoginView.as_view(), name='mlogin'),


]
