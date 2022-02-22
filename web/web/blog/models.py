from django.db import models
from django.db.models.deletion import CASCADE
from category.models import Category
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Blogs(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    content = RichTextUploadingField(verbose_name='content')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    writer = models.CharField(max_length=255)
    views = models.IntegerField(default=0)
    images = models.ImageField(upload_to="blogImages",blank=True)
    create = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(max_length=50)


    def get_url(self):
        return reverse('blogdetail', args=[self.slug])
    
    def __str__(self):
        return self.name 

class Comment(models.Model):
    post = models.ForeignKey(Blogs,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class PhotoAlbum(models.Model):
    picture = models.ImageField(upload_to="pictures",blank=True)
    
    

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.first_name + '  ' + self.last_name 
    

