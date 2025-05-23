from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def machine(request):
    return render(request,'machinelearing/machineLearning.html')



def supervised(request):
    return render(request,'machinelearing/superviesdLearning.html')

def DT(request):
    return render(request,'machinelearing/DT.html')