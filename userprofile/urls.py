from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    path('login/', views.user_login, name='login'), #用户登录
    path('logout/', views.user_logout, name='logout'), #用户退出
    path('register/', views.user_register, name='register'), #用户注册
]