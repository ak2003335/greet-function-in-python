from dataclasses import field
from django import forms
from students.models import Student
class StudentForms(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"