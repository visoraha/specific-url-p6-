from app2.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('madhu/',madhu,name='madhu'),
    path('raju/',raju,name='raju'),
]