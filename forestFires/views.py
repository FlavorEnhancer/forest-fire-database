# defie the views file that is called from the url
# define the http action from the view

from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse('home')
    return render(request, 'homepage.html')


def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')