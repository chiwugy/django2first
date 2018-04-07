# encoding:utf-8

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lists/', views.lists, name='lists'),
    # path('',views., name=''),
]