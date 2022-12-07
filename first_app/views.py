from django.shortcuts import render
from first_app import forms

# Create your views here.


def index(request):
    diction = {
        'title': "Index"
    }
    return render(request, 'first_app/index.html', context=diction)


def student_form(request):
    form = forms.StudentForm()
    diction = {
        'title': "Student Form",
        'student_form': form,
    }
    return render(request, 'first_app/student_form.html', context=diction)
