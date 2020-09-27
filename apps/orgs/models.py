from django.db import models
from datetime import datetime

# Create your models here.
class CityInfo(models.Model):
    name = models.CharField(max_length=20,verbose_name="城市名称")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name ='城市信息'
        verbose_name_plural = verbose_name
        