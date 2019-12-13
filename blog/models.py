from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
# Each Model has a save() function
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
    
    """
    we have passed a parameter to each Field, 
    and the parameter value is the name that the field should display 
    (if not passed, django will automatically generate it based on the field name). 
    The name of this parameter is also called verbose_name
    """
    title = models.CharField(verbose_name='Title',max_length=100)
    # title = models.CharField(max_length=100)
    body = models.TextField(verbose_name='Body Text') #Store rich content

    created_time = models.DateTimeField(verbose_name='Created Time',default=timezone.now)
    modified_time = models.DateTimeField(verbose_name='Modified Time')

    excerpt = models.CharField(verbose_name='Excerpt',max_length=200,blank=True)

    # One article can only map one category while one category can have several articles
    # therefore we use ForeignKey => one to many
    category = models.ForeignKey(Category,verbose_name='Category',on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,verbose_name='Tag',blank=True)

    # User is imported from django.contrib.auth.models
    author = models.ForeignKey(User,verbose_name='Author',on_delete=models.CASCADE)
    
    # Use internal class Meta to configurate model
    class Meta:
        verbose_name = 'Post-Article'
        verbose_name_plural = "Post-Articles"
    
    def save(self,*args,**kwargs):
        self.modified_time = timezone.now()
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title

    # Self define get_absolute_url method
    def get_absolute_url(self):
        # This reverse(), first parametre means
        # a method named detail under the app named blog
        return reverse('blog:detail',kwargs={'pk': self.pk})

