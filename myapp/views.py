from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'myapp/home.html',{'name':'Sunil Kumar'})

def base(request):
    return render(request,'myapp/base.html')

def child(request):
    return render(request,'child.html')

def sam(request):
    return render(request,'myapp/sam.html')
