from django.shortcuts import render
from first_app import forms
from .models import Student

# Create your views here.


def index(request):
    # collecting all the students information in the student_list variable with the following statement
    student_list = Student.objects.all().order_by('first_name')
    diction = {
        'title': "Student List",
        'student_list': student_list,
    }
    # returning the index.html page with the list of students and the title
    # student_list will be handled in the html file
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

    # Creating a student form and sending the to the user
    diction = {
        'title': "Student Form",
        'student_form': form,
    }
    return render(request, 'first_app/student_form.html', context=diction)


def student_info(request, student_id):
    # searching the student with the following statement
    student_info = Student.objects.get(pk=student_id)
    diction = {
        'student_info': student_info,
    }
    return render(request, 'first_app/student_info.html', context=diction)


def student_update(request, student_id):
    # finding the student by the following statement
    student_info = Student.objects.get(pk=student_id)

    # putting all the data into the form to edit that information
    form = forms.StudentForm(instance=student_info)

    # if user hits update button then the method will be "POST"
    if request.method == "POST":
        form = forms.StudentForm(request.POST, instance=student_info)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction = {
        'student_form': form,
    }
    # if the page reloads then return the same page with same data
    return render(request, 'first_app/student_update.html', context=diction)


def student_delete(request, student_id):
    # deleting the student by the following statement
    student = Student.objects.get(pk=student_id).delete()
    diction = {
        'delete_message': "Delete Done",
    }
    return render(request, 'first_app/student_delete.html', context=diction)
