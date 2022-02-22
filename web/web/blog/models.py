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
        return reverse('blogdetail', args=[int(self.pk),self.category.slug,self.slug])
    
    def __str__(self):
        return self.name 

class Comment(models.Model):
    post = models.ForeignKey(Blogs,related_name="comments",on_delete=models.CASCADE)
    name_comment = models.CharField(max_length=255)
    body = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
     self.article_url = Blogs.objects.get(id=self.article_id).get_absolute_url()
     return self.article_url
    
    
    def __str__(self):
        return '%s - %s' %(self.post.name , self.name_comment)


class PhotoAlbum(models.Model):
    picture = models.ImageField(upload_to="pictures",blank=True)
    
    

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.first_name + '  ' + self.last_name 
    

