from django.shortcuts import render
from first_app import forms
from .models import Student

# Create your views here.


def index(request):
    student_list = Student.objects.all().order_by('first_name')
    diction = {
        'title': "Student List",
        'student_list': student_list,
    }
    return render(request, 'first_app/index.html', context=diction)


def student_form(request):
    form = forms.StudentForm()

    # (request.method == "POST") when user clicks on the submit button
    if request.method == "POST":
        form = forms.StudentForm(request.POST)

        if form.is_valid():
            # (commit = True) pushes the forms date into the database
            form.save(commit=True)
            return index(request)
            # calling index() function to return into the index page

    # sending data to the HTML page so that we can access the data and show that data into the web page
    diction = {
        'title': "Student Form",
        'student_form': form,
    }
    return render(request, 'first_app/student_form.html', context=diction)
