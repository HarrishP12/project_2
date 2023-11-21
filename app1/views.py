from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hi(request):
    return HttpResponse('Hi how are u!')