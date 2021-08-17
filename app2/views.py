from django.shortcuts import render

# Create your views here.
def app2_hello(request):
    return render(request,'app2_hello.html')
