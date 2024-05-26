from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,"home.html")

def profile(request):
    return render(request,"profile.html")

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def about(request):
    return render(request,"about.html")

def courses(request):
    return render(request, "courses.html")

def helper(request):
    return render(request, "helper.html")

def update(request):
    return render(request, "update.html")

def meeting(request):
    return render(request, "meeting.html")

def teacher_profile(request):
    return render(request, "teacher_profile.html")