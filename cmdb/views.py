from django.shortcuts import render,redirect,HttpResponse
from cmdb import forms

# Create your views here.


def login(request):
    if request.method == "GET":
        obj = forms.loginform()
        render(request,'login.html',{'form':obj})
    elif request.method == "POST":
        

