from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hey There!What u doin.. u r polls index <input type = 'submit' class = 'ok' caption = 'ok'>")