from django import forms
from .models import Student_Details
from django.forms import TextInput

class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=TextInput(attrs={'type': 'text', 'placeholder': 'Enter Username', 'class': 'form-control'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'Enter Password', 'class': 'form-control'}))

class StudentForm(forms.ModelForm):
    roll_no = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Student_Details
        fields = ['roll_no', 'name', 'age', 'city']