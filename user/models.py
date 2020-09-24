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

    def to_dict(self):
        return{
            'id':self.id,
            'phonenum':self.phonenum,
            'nickname':self.nickname,
            'gender':self.gender,
            'birthday':str(self.birthday),
            'avatar':self.avatar,
            'location':self.location
        }


class Profile(models.Model):
    dating_location= '⽬标城市'
    dating_gender= '匹配的性别'
    min_distance= '最⼩查找范围'
    max_distance= '最⼤查找范围'
    min_dating_age= '最⼩交友年龄'
    max_dating_age= '最⼤交友年龄'
    vibration= '开启震动'
    only_matched= '不让陌⽣⼈看我的相册'
    auto_play= '⾃动播放视频'