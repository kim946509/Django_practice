from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):

    if request.method == "POST":
        return render(request,'accountapp/hello_world.html',context={'text': 'POST METHOD!!!'}) #context: 데이터꾸러미
    else:
        return render(request,'accountapp/hello_world.html',context={'text': 'GET METHOD!!!'})