from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question

def index(req):

    return HttpResponse("index Page");

def test(req):
    return HttpResponse("test")

def user(requ):

    return HttpResponse("user")