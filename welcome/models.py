from email.policy import default
from django.db import models

# Create your models here.
class client(models.Model):
    name=models.CharField(max_length=20,default="")
    age=models.CharField(max_length=20,default="")
    place=models.CharField(max_length=20,default="")
    phone=models.CharField(max_length=20,default="")

