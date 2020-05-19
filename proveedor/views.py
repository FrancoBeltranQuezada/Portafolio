from django.shortcuts import render
from .models import prov
from django.http import HttpResponse

# Create your views here.


def index (request):
    return render(request,'proveedor/index.html')

def aboutt (request):
    return render(request,'proveedor/aboutt.html')

