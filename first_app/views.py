from django.shortcuts import render

# Create your views here.


def index(request):
    diction = {
        'title': "Index"
    }
    return render(request, 'first_app/index.html', context=diction)


def student_form(request):
    diction = {
        'title': "Student Form"
    }
    return render(request, 'first_app/student_form.html', context=diction)
