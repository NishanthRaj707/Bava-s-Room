from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    name=models.CharField(max_length=25)
    content=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
   
    
class Register(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=15)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
   