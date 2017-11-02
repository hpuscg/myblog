from django.db import models


class BaseManager(models.Manager):
    """定义一个模型管理器抽象类"""
    # 获得一个对象
    def get_one_object(self, *args, **kwargs):
        try:
            obj = self.get(*args, **kwargs)
        except:
            obj = None
        return obj

    # 添加一个对象
    def add_one_object(self, *args, **kwargs):
        obj = self.model(*args, **kwargs)
        obj.save()
        return obj

    # 获得所有对象
    def get_all_object(self, filters={}, order_by=('-pk',)):
        obj_list = self.filter(**filters).order_by(*order_by)
        return obj_list
