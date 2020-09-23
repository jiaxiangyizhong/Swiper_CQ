from django.db import models


# Create your models here.
class User(models.Model):
    GENDERS = (
        ('male', '男性'),
        ('female', '女性'),
    )
    LOCATIONS = (
        ('北京', '北京'),
        ('上海', '上海'),
        ('山东', '青岛'),
        ('山东', '济宁'),
    )
    phonenum = models.CharField(max_length=16, unique=True, verbose_name='⼿机号')
    nickname = models.CharField(max_length=20, db_index=True, verbose_name='昵称')
    gender = models.CharField(max_length=10, choices=GENDERS, verbose_name='性别')
    birthday = models.DateField(default='2002-01-01', verbose_name='出⽣⽇')
    avatar = models.CharField(max_length=256, verbose_name=' 个⼈形象')
    location = models.CharField(max_length=10, choices=LOCATIONS, verbose_name='常居地')
