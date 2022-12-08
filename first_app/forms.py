from django import forms
from first_app import models


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = "__all__"

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
