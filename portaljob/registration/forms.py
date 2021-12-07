from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(max_length=69,label='User name')
    password=forms.CharField(max_length=69,label='password',widget=forms.PasswordInput)