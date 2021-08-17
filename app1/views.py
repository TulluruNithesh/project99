from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_hai(request):
    return render(request,'app1_hai.html')


def string_s(request):
    return HttpResponse('this is geniric')