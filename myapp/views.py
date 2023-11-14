from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hello():
    return HttpResponse("Hello world ! ")