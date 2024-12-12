from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    x=1
    y=2
    z=x+y
    print("value:",z)
    # return HttpResponse("Hello World")
    return render(request, 'hello.html',{'name':'Tom'})