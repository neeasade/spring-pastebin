from django.db import models

# Create your models here.

class Paste(models.Model):
    content = models.CharField(max_length=65535)
    title = models.CharField(max_length=30)
    views = models.IntegerField(default=0)

class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

