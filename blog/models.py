from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import markdown
from django.utils.html import strip_tags

# Create your models here.
#分类类
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#标签类
class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#文章类
class Post(models.Model):
    title = models.CharField('标题', max_length=100)
    body = models.TextField('正文')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    modified_time = models.DateTimeField('修改时间')
    excerpt = models.CharField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    class Meta:   #model特性由在内部Meta类中定义
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()

        # 首先实例化一个Markdown类，用于渲染body的文本
        # 由于摘要并不需要生成文章目录，所以去掉了目录拓展
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

        # 先将Markdown文本渲染成HTML文本
        # strip_tags 去掉HTML文本的全部HTML标签
        # 从文本摘取前60个字符赋给excerpt
        self.excerpt = strip_tags(md.convert(self.body))[:82]

        super().save(*args, **kwargs)

    #自定义get_absolute_url方法生成文章自己的url
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})