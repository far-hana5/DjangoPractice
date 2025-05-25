from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def machine(request):
    course="machine learning"
    tClass=21
    seat=20
    cDuration='2.5 months'
    offering={'c':course,'tc':tClass,'st':seat,'cd':cDuration}
    Teachers={'names':['far','fahi','hana']}
   # return render(request,'machinelearing/machineLearning.html',context=offering)
    return render(request,'machinelearing/machineLearning.html',context=Teachers)


def supervised(request):
    return render(request,'machinelearing/superviesdLearning.html')

def DT(request):
    return render(request,'machinelearing/DT.html')