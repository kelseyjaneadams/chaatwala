from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def reviews_home(request):
    return HttpResponse("Hello, Reviews!")