from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
     return render(request, 'home.html')

def aboutus(request):
     return render(request,'aboutus.html')

def family(request):
     return render(request,'family.html')

def contactus(request):
     return render(request,'contactus.html')

def news(request):
     return render(request,'news.html')

def stores(request):
     return render(request,'stores.html')