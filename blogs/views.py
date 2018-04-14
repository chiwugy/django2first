from django.shortcuts import render

#from .models import User

#from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'blogs/index.html')

def lists(request):
    return render(request, 'blogs/list.html')

def details(request):
    return render(request, 'blogs/list.html')
