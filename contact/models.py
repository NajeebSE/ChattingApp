
import email
from email.message import EmailMessage
from django.db import models
#from django.contrib.auth.models import User
import datetime


#contact model
class contact_model(models.Model):
    username = models.CharField(max_length=700)
    email = models.EmailField(max_length=40, null=True)
    message = models.TextField(max_length=500)
    
    def __str__(self):
        return self.username

#feedback model
class feedback_model(models.Model):
    username = models.CharField(max_length=700)
    meet = models.CharField(max_length=40)
    better = models.TextField(max_length=500)
    
    def __str__(self):
        return self.username


# example
class exmple(models.Model):
    yourname = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
