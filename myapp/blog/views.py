from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,Register
from .forms import UploadForm,RegisterForm,LoginForm
from django.urls import reverse
# Create your views here.


def index(request):
    return render(request,'main.html')
def home(request):
    posts=Post.objects.all() 
    return render(request,'home.html',{'posts':posts})
def personal(request):
    return render(request,'personal.html') 
def detail(request,id):
    posts=Post.objects.get(pk=id)
    return render(request,'target.html',{'posts':posts})   
def upload(request):
    if request.POST:
        form=UploadForm(request.POST)
        if  form.is_valid():
            form.save()
            print('Data uploaded')
    return render(request,'upload.html')
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid(): 
            print("validate")   
            form.save()
            return redirect(reverse('blog:login'))
        print(form.is_valid())
    else:
        form=RegisterForm()
        
    return render(request,'register.html',{'form':form})
def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            data=Register.objects.get(username=form.cleaned_data['username'])
            if data:
                if data.password==form.cleaned_data['password']:
                    return redirect(reverse('blog:home'))

    return render(request,'login.html')