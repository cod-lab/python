from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('',views.fn1,name='fn1'),
]