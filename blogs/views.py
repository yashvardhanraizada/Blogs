from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import User

def default(request):
    return HttpResponseRedirect('/blogs/')

def index(request):
    return render(request, 'blogs/index.html')