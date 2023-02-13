import imp
from operator import mod
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.db import models
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilepic = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class blog_model(models.Model):
    img = models.ImageField(upload_to="blogspic")
    title = models.CharField(max_length = 150)
    description = models.CharField(max_length = 700)
   
    
    def __str__(self):
        return self.title

class Moreblog(models.Model):
    img = models.ImageField(upload_to="blogspic")
    title = models.CharField(max_length = 150)
    description = models.CharField(max_length = 700)
    time = models.DateTimeField( auto_now=False, auto_now_add=False)
    
    
    def __str__(self):
        return self.title





