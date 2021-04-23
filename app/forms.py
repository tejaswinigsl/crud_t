from django import forms
from app.models import  Employee1



class EmployeeForm1(forms.ModelForm):
    class Meta:
        model=Employee1
        fields='__all__'
