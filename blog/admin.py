from django.contrib import admin
from .models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # list_display控制文章列表展示字段
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    # fields控制文章表单展示字段
    fields = ['title', 'body', 'created_time', 'category', 'tag']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

#模型注册，models中的数据库模型只有在admin文件中注册才能在django后台显示
admin.site.register(Category)
admin.site.register(Tag)
