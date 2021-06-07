from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.shortcuts import render
def index(req):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(req, 'pages/question_list.html',context)

def test(req):
    return HttpResponse("test")

def user(requ):

    return HttpResponse("user")