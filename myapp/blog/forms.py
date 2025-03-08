from django import forms
from blog.models import Post,Register

#form for uploads
class UploadForm(forms.ModelForm):
    title=forms.CharField(max_length=50)
    name=forms.CharField(max_length=50)
    content=forms.CharField()

    class Meta:
        model=Post
        fields=['title','name','content']

class RegisterForm(forms.ModelForm):
    username=forms.CharField(label="username",max_length=50)
    email=forms.EmailField(label="email")
    password=forms.CharField(label="password",max_length=15)
    
    class Meta:
        model=Register
        fields=['username','email','password']
class LoginForm(forms.Form):
    username=forms.CharField(label="username",max_length=50)
    password=forms.CharField(label="password",max_length=15)
    