from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def main_view(request):
    context = {}

    return render (request, 'main.html', context=context)

# def getid(self,request, **kwargs):
#     getuserid = User.objects.filter(pk=self.kwargs.get('pk'))
#     return render(request, 'main.html',{'getuserid':getuserid})

