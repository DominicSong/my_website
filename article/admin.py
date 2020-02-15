from django.contrib import admin

from .models import ArticlePost
# Register your models here.

# 注册model到admin
admin.site.register(ArticlePost)