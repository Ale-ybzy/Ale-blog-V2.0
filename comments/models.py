from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
# 引入 User 模型
from django.contrib.auth.models import User


class Comment(models.Model):
    #name = models.CharField('名字', max_length=50)
    name = models.ForeignKey(User, verbose_name='用户名', on_delete=models.CASCADE)
    email = models.EmailField('邮箱', blank=True)
    #email = models.ForeignKey(User, verbose_name='邮箱', on_delete=models.CASCADE)
    url = models.URLField('网址', blank=True)
    text = RichTextField('内容')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    post = models.ForeignKey('blog.Post', verbose_name='文章', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])