from django.db import models

# Create your models here.
from django.db import models
class employee(models.Model):
    name=models.CharField(max_length=32,verbose_name='姓名')
    email=models.EmailField(verbose_name='邮箱')
    dep=models.ForeignKey(to='department',on_delete=models.CASCADE)
    salary=models.DecimalField(max_digits=8,decimal_places=2)
    info=models.OneToOneField(to='employee',on_delete=models.CASCADE,null=True)
class department(models.Model):
    dep_name=models.CharField(max_length=32,verbose_name='部门名称')
    dep_script=models.CharField(max_length=60,verbose_name="备注")
    #id=models.IntegerField(verbose_name="用户id")
class group(models.Model):
    group_name=models.CharField(max_length=32,verbose_name='团体名称')
    group_script=models.CharField(max_length=60,verbose_name="备注")
class employinfo(models.Model):
    phtone=models.CharField(max_length=11)
    address=models.CharField(max_length=50)
