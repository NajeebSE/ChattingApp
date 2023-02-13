import email
import imp
from pyexpat import model
from django.shortcuts import render
from team.models import team_member
from blogs.models import blog_model, Moreblog 
from contact.models import contact_model
from contact.models import feedback_model
from postblog.models import user_post
from postblog.forms import editForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# registration logic
def register(request):
    
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:
            messages.warning(request, 'password does not match')
            return redirect('register')

        elif User.objects.filter(username=uname).exists():
            messages.warning(request, 'user name is exits')
            return redirect('register')

        elif User.objects.filter(email=email).exists():
            messages.warning(request, 'email is already taken')
            return redirect('register')
        else:
            user = User.objects.create_user(first_name=fullname,  username=uname ,email=email, password=pass1)
            user.save()
            messages.success(request, 'User hase been register succssfully')
        return redirect('userlogin')
            
            
    return render(request, 'register.html')


# login logic 

def userlogin(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        
        else:
            messages.warning(request,'User is Not Registered')
            return redirect('register')
    return render(request, 'login.html')


# Logout logic
def userlogout(request):
    logout(request)
    return redirect('/')



#Login for Home page  
def Homesection(request):
    userdata = User.objects.all()
   
    return render(request, "home.html", {'userdata':userdata})

def about(request):
    team = team_member.objects.all()
    teamdata ={
        'team':team
    }
    return render(request, "about.html",teamdata)
    
# logic for blogs page
def blogfun(request):
   
    moreblogs = Moreblog.objects.all()
    data = user_post.objects.all()
    moreblogs = {
        'moreblogs':moreblogs,
        'data':data
    }
   
    return render(request, "blog.html",moreblogs)

def vision(request):
    return render(request, "vision.html", {})




def contact(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contactdata = contact_model(username=username, email=email, message=message)
        contactdata.save()
        messages.success(request, 'your message is successfully send')
        return redirect('/')
    
    return render(request, "contact.html", {})
    

#feedback logic
def feedback(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        meet = request.POST.get('meet')
        better = request.POST.get('better')
        feedbackdata = feedback_model(username=username, meet=meet, better=better)
        feedbackdata.save()
        messages.success(request, 'your feedback is sended. thank you')
        return redirect('/')   
    return render(request, "feedback.html" )

    #post blog .............
def postblog(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        dsc = request.POST.get('dsc')
        postblogbyuser = user_post(title=title, dsc=dsc, user_id=request.user)
        postblogbyuser.save()
        messages.success(request, 'blog is successfully post')
        return redirect('/')

    return render(request, 'post.html')

def delete(request, id):
    blogs = user_post.objects.get(id = id).delete()
    messages.success(request,"Your Blog is deleted...")
    return redirect('/')
    
def edit(request, id):
    employee =  user_post.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})

def update(request, id):
    employee = user_post.objects.get(id=id)
    form = editForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'edit.html', {'employee': employee})


def searchd(request):
    if request.method == 'GET':
            query = request.GET.get('query')
            if query:
                blogname = Moreblog.objects.filter(title__icontains=query)
                return render(request, "searchd.html", {'blogname':blogname}) 

            else:
                print("no information")
                return request(request, "searchd.html")


    
    

    
    