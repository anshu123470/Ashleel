from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('', views.index),
    path('index/photo/', views.photo),
    path('video/<slug>/', views.playpage, name='video'),
    path('search/', views.search, name='search'),

]