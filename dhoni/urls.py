from django.urls import path
from dhoni.views import *
app_name='dhoni'

urlpatterns=[
    path('csk/',csk,name='csk'),
]