from django import forms

class Signin(forms.Form):
    username = forms.CharField(label='', max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput, label='Password')
class Signup(forms.Form):
    username = forms.CharField(label='User name', max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput,label="Password")