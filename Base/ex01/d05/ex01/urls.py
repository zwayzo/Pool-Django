from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('django', views.django, name='django'),
    path('display', views.display, name='display'),
    path('templates', views.templates, name='templates'),
    # path('', include('ex01.urls')),
]
