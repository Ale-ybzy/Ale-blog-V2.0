from django import template
from django.db.models.aggregates import Count
from ..models import Post, Category, Tag
from accstat.models import VisitNumber, DayNumber

register = template.Library()


# 最新文章模板标签
@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_post_list': Post.objects.all().order_by('-created_time')[:num],
    }


# 归档模板标签
@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Post.objects.dates('created_time', 'month', order='DESC'),

    }


# 分类模板标签
@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    # return {
    #     'category_list': Category.objects.all(),
    #     'category.num_posts': Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    # }
    category_list = Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    return {
        'category_list': category_list,
    }


# 标签云模板标签
@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    # return {
    #     'tag_list': Tag.objects.all(),
    #
    # }
    tag_list = Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    return {
        'tag_list': tag_list,
    }


# 访问统计标签
@register.inclusion_tag('blog/inclusions/_stat.html', takes_context=True)
def show_stat(context):
    day_list = DayNumber.objects.all().order_by('-day')
    visit_list = VisitNumber.objects.all()
    return {
        'day_list': day_list,
        'visit_list': visit_list,
    }
