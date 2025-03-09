from  django.urls import path
from . import views
app_name='blog'
urlpatterns=[
    path("",views.index,name="main"),
    path("home",views.home,name='home'),
    path('personal',views.personal,name='personal'),
    path("detail/<int:id>",views.detail,name='detail'),
    path("register",views.register,name='register'),
    path("upload",views.upload,name='upload'),
    path("login",views.login,name="login")
]