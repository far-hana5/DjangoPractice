from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def machine(request):
    return HttpResponse("Hello, Django App!")


