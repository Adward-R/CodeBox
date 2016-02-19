__author__ = 'Adward'
from django.db import models
from django.conf import settings
class WeiboData(models.Model):
    index = models.IntegerField(primary_key=True)
    level1 = models.IntegerField(default=10)
    level2 = models.IntegerField(default=10)
    level3 = models.IntegerField(default=10)