from django.db import models
from django.forms import ImageField

class team_member(models.Model):
    img = models.ImageField(upload_to="teampic")
    title = models.CharField(max_length = 150)
    description = models.CharField(max_length = 150)
    
    
    def __str__(self):
        return self.title

