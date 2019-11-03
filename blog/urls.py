from django.urls import path

from . import views

#url模型
urlpatterns = [
    path('', views.index, name='index'),
]