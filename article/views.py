from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    artics = ArticlesInfo.objects.all()
    context = {'artics':artics}
    return render(request, 'daydays/arite/index.html',context)

def detail(request,pk):
    artics = ArticlesInfo.objects.get(id=pk)
    context = {'artics':artics}
    return render(request, 'daydays/arite/detail.html',context)

def list(request):
    artics = ArticlesInfo.objects.all()
    context = {'artics':artics}
    return render(request, 'daydays/arite/list.html',context)
