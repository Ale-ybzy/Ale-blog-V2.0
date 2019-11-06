from django.urls import path

from . import views

#url模型
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'), #首页
    path('posts/<int:pk>/', views.detail, name='detail'), #详情页
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'), #归档页
    path('categories/<int:pk>/', views.category, name='category'), #分类页
    path('tags/<int:pk>/', views.tag, name='tag'),  #标签页
]