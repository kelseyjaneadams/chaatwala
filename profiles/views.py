from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def profile_view(request):
    return HttpResponse("Profile page is working!")