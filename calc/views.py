from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render (request,'home.html',{'name':'shanthu'})
def add(request):
    value1=int(request.POST['first'])
    value2=int(request.POST['second'])
    res= value1+value2


    return render(request,'result.html',{'result':res})