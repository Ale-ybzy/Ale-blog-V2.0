from django.utils import timezone

from django.db import models


# 访问网站的 ip 地址、端点和次数
class UserIP(models.Model):
    ip = models.CharField(verbose_name='IP 地址', max_length=30)
    ip_addr = models.CharField(verbose_name='IP 地理位置', max_length=30)
    end_point = models.CharField(verbose_name='访问端点', default='/', max_length=30)
    count = models.IntegerField(verbose_name='访问次数', default=0)

    class Meta:
        verbose_name = '访问用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip


# 网站总访问次数
class VisitNumber(models.Model):
    count = models.IntegerField(verbose_name='网站访问总次数', default=0)  # 网站访问总次数

    class Meta:
        verbose_name = '网站访问总次数'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.count)


# 单日访问量统计
class DayNumber(models.Model):
    day = models.DateField(verbose_name='日期', default=timezone.now)
    count = models.IntegerField(verbose_name='网站访问次数', default=0)  # 网站访问总次数

    class Meta:
        verbose_name = '网站日访问量统计'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.day)
