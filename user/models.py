from django.db import models

# Create your models here.

#管理员表
class ManageUser(models.Model):
    u_username = models.CharField(unique=True, max_length=32)
    u_password = models.CharField(max_length=256)
    u_email = models.CharField(unique=True, max_length=64)
    is_active = models.IntegerField(default=1)
    is_delete = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'manage_user'



#用户表
class CartoonUser(models.Model):
    u_username = models.CharField(unique=True, max_length=32)
    u_password = models.CharField(max_length=256)
    u_email = models.CharField(unique=True, max_length=64)
    is_active = models.IntegerField(default=1)
    is_delete = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'cartoon_user'

#漫画类型表
class Cartoontype(models.Model):
    typeid = models.IntegerField()
    typename = models.CharField(max_length=32)


    class Meta:
        # managed = False
        db_table = 'cartoontype'

#漫画简介表
class Cartoons(models.Model):
    ctitle = models.CharField(max_length=200)
    cpub_date = models.DateField(blank=True, null=True)
    cauth = models.CharField(max_length=200)
    cimage = models.CharField(max_length=200, blank=True, null=True)
    ctype_id = models.ForeignKey(Cartoontype,models.DO_NOTHING, db_column='tid', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'cartooninfo'

#漫画展示表
class CartoonShow(models.Model):
    sid = models.AutoField(primary_key=True)
    sinfo = models.CharField(max_length=5000)
    shero = models.CharField(max_length=50)
    cweb = models.CharField(max_length=2000)
    cid = models.ForeignKey(Cartoons, models.DO_NOTHING, db_column='cid', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'cartoonshow'

#喜欢的漫画表
class Cartoonlike(models.Model):
    c_cartoons_num = models.IntegerField()
    c_is_select = models.IntegerField()
    c_cartoons = models.ForeignKey('Cartoons', models.DO_NOTHING, blank=True, null=True,related_name='likes')
    c_user = models.ForeignKey('CartoonUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'cartoonlike'


