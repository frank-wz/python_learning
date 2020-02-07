from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=12)
    password = models.CharField(max_length=20)
    
# 出版社
class Publisher(models.Model):
    pname = models.CharField(max_length=12)
    addr = models.TextField()