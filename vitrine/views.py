from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vitrine(request):
    return HttpResponse("Você está na vitrine")

