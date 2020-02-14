from django.shortcuts import render as r
from django.http import HttpResponse as hr

# Create your views here.
def index(request):
    return HttpResponse("hey There!What u doin.. u r polls index")