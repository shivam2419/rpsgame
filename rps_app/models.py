from django.db import models

# Create your models here.
class Info(models.Model):
    sname=models.CharField(max_length=100)
    roll=models.CharField(max_length=200)
    score=models.IntegerField(default=0)
    status=models.CharField(max_length=10)
