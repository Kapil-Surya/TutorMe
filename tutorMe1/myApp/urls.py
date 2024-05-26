from django.urls import path
from . import views

urlpatterns = [
    path("home.html/",views.home, name ="home"),
    path("",views.home,name = "home"),
    path("profile.html/",views.profile, name = "profile"),
    path("login.html/",views.login, name = "login" ),
    path("register.html/",views.register, name = "register"),
    path("teacher_profile.html/",views.teacher_profile, name = "teacher_profile"),
    path("courses.html/", views.courses, name = "courses"),
    path("about.html/", views.about, name = "about"),
    path("helper.html/", views.helper, name = "helper"),
    path("update.html/", views.update, name = "update"),
    path("meeting.html/", views.meeting, name = "meeting")

]