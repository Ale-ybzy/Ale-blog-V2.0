from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
'''
def index(request):  #request参数为django封装好的http请求，它为类HttpRequest的一个实例
    return HttpResponse("欢迎访问我的博客首页！")  #HttpResponse是类HttpResponse的一个实例
'''
'''
def index(request):
    return render(request, 'blog/index.html', context={  #render函数根据传入参数构造HttpResponse
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客首页'
    })
'''

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
