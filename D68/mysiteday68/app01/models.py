from django.db import models

# Create your models here.

# 用户表
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True) # 在数据库中生成自增的ID主键字段
    email = models.CharField(max_length=20)  #varchar(20)
    password = models.CharField(max_length=30)  #varchar(20)

    
# 出版社表
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16) # varchar（16）
    
    def __str__(self):
        return self.name

# 书籍
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20) # 书名
    publisher = models.ForeignKey(to='Publisher')   # ORM自动给外键字段加_id

    def __str__(self):
        return '<{}>'.format(self.title)
# 作者