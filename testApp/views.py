from django.shortcuts import render

# Create your views here.

def home_page(req):
    return render(req, "pages/home.html")

