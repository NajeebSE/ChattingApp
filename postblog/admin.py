from atexit import register
import imp
from django.contrib import admin
from .models import user_post

admin.site.register(user_post)
# Register your models here.
