from django.contrib import admin
from .models import UserIP, VisitNumber, DayNumber


# Register your models here.
class UserIPAdmin(admin.ModelAdmin):
    list_display = ['ip', 'ip_addr', 'count', 'end_point']


class DayNumberAdmin(admin.ModelAdmin):
    list_display = ['day', 'count']


admin.site.register(DayNumber, DayNumberAdmin)
admin.site.register(VisitNumber)
admin.site.register(UserIP, UserIPAdmin)
