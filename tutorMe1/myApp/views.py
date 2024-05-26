from django.shortcuts import redirect, render, HttpResponse
from django.contrib import auth, messages
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from .models import Course


# Create your views here.

#def course_list(request):

courses = [
    Course(
        name = "HTML Tutorial",
        tutor = "Sneha Subbarayudu"
    ),
    Course(
        name = "CSS and JS Tutorial",
        tutor = "Kapil Surya"
    ),
    Course(
        name = "Java Tutorial",
        tutor = "Samaya Argula"
    )
]


#results = Course.objects.bulk_create(courses)

def home(request):
    return render(request,"home.html")

def profile(request):
    return render(request,"profile.html")

def login(request):
    if request.method == 'post':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            messages.error(request, "Invalid login details")

    return render(request,"login.html",{"form": LoginForm})

def register(request):
    #if request.method == "post":
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('/home')
        
       
    else:
        form = RegisterForm()
               
    return render(request,"register.html",{"form":form})

def about(request):
    return render(request,"about.html")

def courses(request):
    my_data = Course.objects.all()
    return render(request, "courses.html")

def helper(request):
    return render(request, "helper.html")

def update(request):
    return render(request, "update.html")

def meeting(request):
    return render(request, "meeting.html")

def teacher_profile(request):
    return render(request, "teacher_profile.html")