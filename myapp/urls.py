from django.urls import path
from .views import main_view


urlpatterns = [
    path('main_view/', main_view, name='main_view'),
 
]