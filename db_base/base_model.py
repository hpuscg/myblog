from django.db import models


class BaseModel(models.Model):
    """定义一个模型抽象类"""
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        abstract = True
