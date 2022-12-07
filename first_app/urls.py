from django.urls import path
from . import views

app_name = "first_app"

urlpatterns = [
    path('', views.index, name="index"),
    path('student_form', views.student_form, name="student_form"),
]
