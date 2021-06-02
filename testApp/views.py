from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(req):
    return HttpResponse("index Page");

def test(req):
    return HttpResponse("test")

def user(requ):
    return HttpResponse("user")