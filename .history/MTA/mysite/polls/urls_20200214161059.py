from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('fn1/',views.fn1,name='fn2'),
]