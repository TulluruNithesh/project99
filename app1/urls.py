from django.urls import path
from app1.views import *

app_name = 'app1_hai'

urlpatterns = [
    path('app1_hai/',app1_hai,name='app1_hai'),
]