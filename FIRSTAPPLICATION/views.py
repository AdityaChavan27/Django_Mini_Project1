from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Hello I am in home")

def hello(request):
    return render(request,'hello.html')