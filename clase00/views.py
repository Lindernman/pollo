from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request, 'clase00/index.html')

def home(request):
    return render(request, 'clase00/home.html')
def tabla(request):
    return render(request, 'clase00/tabla.html')
