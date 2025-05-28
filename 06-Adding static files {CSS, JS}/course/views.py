from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'course/django.html', context={'name': "Rohan"})