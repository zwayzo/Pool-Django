from django.urls import path
from . import views

urlpatterns = [
    path('ex00', views.index, name='index'),
    path('ex02', views.test, name='test'),
]
