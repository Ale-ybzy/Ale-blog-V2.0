from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Category, Tag
import markdown
from markdown.extensions.toc import TocExtension
import re
from django.utils.text import slugify
from django.views.generic import ListView
from django.contrib import messages

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
'''
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
'''
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    # 指定 paginate_by 属性后开启分页功能，其值代表每一页包含多少篇文章
    paginate_by = 8

#详情页视图函数
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 阅读量+1
    post.increase_views()

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
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                   ).order_by('-created_time')
    # post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


class ArchivesView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year,
                                                               created_time__month=month
                                                               )

#分类页面视图

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


class CategoryView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


#标签页面视图
def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tag=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

#文章搜索视图函数
def search(request):
    q = request.GET.get('q')

    if not q:
        error_msg = "请输入搜索关键词"
        messages.add_message(request, messages.ERROR, error_msg, extra_tags='danger')
        return redirect('blog:index')

    post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'blog/index.html', {'post_list': post_list})

#自我简介页面
def about(request):
    return render(request,'blog/about.html')

#友情链接界面
def blogroll(request):
    return render(request,'blog/blogroll.html')
