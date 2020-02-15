from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class ArticlePost(models.Model):
    # 外键，是另一个表的主键。on_delete控制删除外键后本表的行为
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    # auto_now即为每次更新时写入当前时间
    updated = models.DateTimeField(auto_now=True)

    # Django内部Meta类定义模型类的相关特性
    class Meta:
        # 返回记录结果集依照什么字段排序，前面加‘-’是倒序
        ordering = ('-created',)

    def __str__(self):
        return self.title