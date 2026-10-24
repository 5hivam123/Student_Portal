from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_home, name="student_home"),
    path("about/", views.about_page, name="about_page"),
]