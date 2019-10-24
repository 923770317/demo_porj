# -*- coding: utf-8 -*- 
# @Time : 2019-10-08 23:36 
# @Author : derek.zhang 
# @File : urls.py 
# @Software: PyCharm

from django.urls import path
from demo_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/<str:country_name>/', views.hello_country, name='hello'),
    path('add/', views.add, name='add'),
]