from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hey There!What u doin.. u r polls index <br> <input type = 'submit' class = 'ok' caption = 'ok'>")

def fn1(request):
    return HttpResponse("hey There!this is fn1<br> <input type = 'submit' class = 'ok' caption = 'ok buddy'>")