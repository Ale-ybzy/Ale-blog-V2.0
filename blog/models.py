from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import markdown
from django.utils.html import strip_tags
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


# 分类类
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 标签类
class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 文章类
class Post(models.Model):
    title = models.CharField('标题', max_length=100)
    #body = models.TextField('正文')
    #body = RichTextField('正文')
    body = RichTextUploadingField('正文')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    modified_time = models.DateTimeField('修改时间')
    excerpt = models.CharField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    # 新增view字段记录阅读量
    views = models.PositiveIntegerField(default=0, editable=False)

    class Meta:  # model特性由在内部Meta类中定义
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

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
        self.excerpt = strip_tags(md.convert(self.body))[:100]

        super().save(*args, **kwargs)

    # 自定义get_absolute_url方法生成文章自己的url返回给浏览器
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    # views值递增模型方法
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

# 媒体类
# class Media(models.Model):
#     m_title = models.CharField('标题', max_length=100)
#     m_body = models.TextField('正文')
#     m_created_time = models.DateTimeField('创建时间', default=timezone.now)
#     m_modified_time = models.DateTimeField('修改时间')
#     m_author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
#     m_views = models.PositiveIntegerField(default=0, editable=False)
#
#     class Meta:  # model特性由在内部Meta类中定义
#         verbose_name = '媒体'
#         verbose_name_plural = verbose_name
#         ordering = ['-created_time']
#
#     def __str__(self):
#         return self.m_title
#
#     # 自定义get_absolute_url方法生成媒体资源的url返回给浏览器
#     def get_absolute_url(self):
#         return reverse('blog:detail', kwargs={'pk': self.pk})
#
#     # views值递增模型方法
#     def increase_views(self):
#         self.views += 1
#         self.save(update_fields=['views'])

# 碎碎念类
class Talk(models.Model):
    text = RichTextField('内容')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    name = models.ForeignKey(User, verbose_name='', on_delete=models.CASCADE)

    class Meta:  # model特性由在内部Meta类中定义
        verbose_name = '碎碎念'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    #该函数可以让显示的数据更为直观
    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])