from django.urls import path
from kohli.views import *
app_name='kohli'
urlpatterns=[
    path('rcb/',rcb,name='rcb'),
]