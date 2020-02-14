from django.urls import path as p 
from . import views

urlpatterns = [
    path('',views.index,name='index')
]