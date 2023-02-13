
from django import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('register/',views.register, name="register"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/',views.userlogout, name="userlogout"),
    path('', views.Homesection, name="Homesection"),
    path('blog',views.blogfun, name="blog"),
    path('about/', views.about, name="about"),
    path('vision/', views.vision, name="vision"),
    path('contact/', views.contact, name="contact"),
    path('search/', views.searchd, name="search"),
    path('feedback/', views.feedback, name="feedback"),
    path('postblog/', views.postblog, name="postblog"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('edit/<int:id>', views.edit,name="edit"),
    path('update/<int:id>', views.update, name="update"),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    