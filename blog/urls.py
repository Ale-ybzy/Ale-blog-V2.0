from django.urls import path

from . import views

#url模型
app_name = 'blog'
urlpatterns = [
    # path('', views.index, name='index'), #首页
    path('', views.IndexView.as_view(), name='index'), #首页
    path('posts/<int:pk>/', views.detail, name='detail'), #详情页
    #path('archives/<int:year>/<int:month>/', views.archive, name='archive'), #归档页
    #path('archives/<int:year>/<int:month>/', views.ArchivesView.as_view(), name='archive'), #归档页
    #path('categories/<int:pk>/', views.category, name='category'), #分类页
    path('categories/<int:pk>/', views.CategoryView.as_view(), name='category'), #分类页
    path('tags/<int:pk>/', views.tag, name='tag'),  #标签页
    path('search/', views.search, name='search'),  #搜索页
    path('about/', views.about, name='about'),  #自我简介html页
    path('blogroll/', views.blogroll, name='blogroll'),  #博客推荐html页面
    path('archivehtml/', views.archivehtml, name='archivehtml'),  #归档html页面

]