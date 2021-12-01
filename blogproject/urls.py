"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .settings import common

urlpatterns = [
    path('admin/', admin.site.urls),
    # http:127.0.0.1:8000/admin/
    path('', include('blog.urls')),  #使用include函数将blog下的urls文件包含进来
    path('', include('comments.urls')), #评论应用url文件
    path('ckeditor/', include('ckeditor_uploader.urls')), #
    path('userprofile/', include('userprofile.urls', namespace='userprofile')), # 用户管理
]
# urlpatterns += static(common.MEDIA_URL, document_root=common.MEDIA_ROOT)
urlpatterns += static(common.MEDIA_URL, document_root=common.MEDIA_ROOT)
