from django.shortcuts import render

# Create your views here.

def home_page(req):
    return render(req, "pages/home.html")

def register_board(req):
    return render(req, "pages/register_board.html")

def login(req):
    return render(req, "pages/login.html")

def sign_up(req):
    return render(req, "pages/sign_up.html")
