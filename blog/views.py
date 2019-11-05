from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
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