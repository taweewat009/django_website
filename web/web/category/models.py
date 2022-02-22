from django.db import models
from django.db.models.deletion import CASCADE
import uuid
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(unique=True,default=uuid.uuid1)
    
    
    def get_url(self):
        return reverse('category', args=[self.slug])
    
    def __str__(self):
        return self.name 

