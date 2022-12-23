from django import forms
from first_app import models


class StudentForm(forms.ModelForm):
    class Meta:
        # taking all the fields and creating a form according to the Student object
        model = models.Student

        # telling django that we need all the fields to create the student form
        fields = "__all__"

        # that is how we can put bootstrap class as attributes to style the html form
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
