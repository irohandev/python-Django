from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_Django(req):
    return HttpResponse('<h1>Hello Django from course app!</h1>')