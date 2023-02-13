from django.contrib import admin
from . models import blog_model, Moreblog, Profile



admin.site.register(blog_model)
admin.site.register(Moreblog)
admin.site.register(Profile)