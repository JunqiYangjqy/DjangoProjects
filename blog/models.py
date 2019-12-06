from django.db import models
from django.contrib.auth.model import User
# Create your models here.
# One Class => one table
class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField() #Store rich content
