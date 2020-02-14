from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {}
    context['text'] = "Hello, world!"
    return render(request, 'home.html', context)