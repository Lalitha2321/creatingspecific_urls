from rcb.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('boome/',boome,name='boome'),
]