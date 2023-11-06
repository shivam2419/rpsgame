
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', index),
    path('info', info),
    path('play', play),
    path('end', end),
    path('index', index),
               
]
