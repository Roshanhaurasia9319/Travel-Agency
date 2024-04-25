from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    return render(request,'index.html')

def index2(request):
    return render(request,'index2.html')


def register(request):
    return render(request,'register.html')

def about(request):
    return render(request,'about.html')

def vrindavan(request):
    return render(request,'vrindavan.html')

def mathura(request):
    return render(request,'mathura.html')

def ayodhya(request):
    return render(request,'ayodhya.html')

def rajasthan(request):
    return render(request,'rajasthan.html')