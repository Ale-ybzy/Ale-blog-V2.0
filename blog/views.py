from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category, Tag
import markdown
from markdown.extensions.toc import TocExtension
import re
from django.utils.text import slugify

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

#首页视图函数
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

#详情页视图函数
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
                              'markdown.extensions.extra',
                              'markdown.extensions.codehilite',
                               #'markdown.extensions.toc',
                              TocExtension(slugify=slugify),
                                  ])
    post.body = md.convert(post.body)

    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request, 'blog/detail.html', context={'post': post})

#归档页面视图
def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,  #Python 中调用属性的方式通常是 created_time.year，但是由于这里作为方法的参数列表，所以 django 要求我们把点替换成了两个下划线，即 created_time__year
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

#分类页面视图
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})

#标签页面视图
def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tag=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})