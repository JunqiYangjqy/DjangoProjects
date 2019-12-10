from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# One Class => one table
# All tables(classes) must inherit from models.Model
# id will be created by Django automatically
class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField() #Store rich content

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=200,blank=True)

    # One article can only map one category while one category can have several articles
    # therefore we use ForeignKey => one to many
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,blank=True)

    # User is imported from django.contrib.auth.models
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    # Use internal class Meta to configurate model
    class Meta:
        verbose_name = 'Post-Article'
        verbose_name_plural = "Post-Articles"
    
    def __str__(self):
        return self.title

