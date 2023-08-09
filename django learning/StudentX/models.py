
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=30)
    roll=models.IntegerField()
    age=models.IntegerField()
    address=models.CharField(max_length=80)
    phone=models.IntegerField()
    email=models.EmailField()
    photo=models.ImageField(upload_to="imagedata")