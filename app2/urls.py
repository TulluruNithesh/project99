from django.urls import path
from app2.views import *

app_name = 'app2_hello'

urlpatterns = [
    path('app2_hello/',app2_hello,name='app2_hello'),
]