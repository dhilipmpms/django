from django.shortcuts import render
import datetime 
from django.http import HttpResponse,HttpResponseNotFound
from django.views.decorators.http import require_http_methods


# def index(request):

#     return render(request,'index.html')


# def submit(request):

#     mobile=int(request.GET[('mobile')])
#     tws=int(request.GET[('tws')])
#     case=int(request.GET[('case')])
#     result=mobile+tws+case

#     return render(request,'submit.html',{'mobile':mobile,'tws':tws,'case':case,'price':result})

def index(request):
    return render(request,'index.html')


def register(request):
    name=request.POST[('name')]
    password=request.POST[('password')]
    address=request.POST[('address')]
    mail=request.POST[('mail')]

    return render(request,'submit.html',{'name':name,'password':password,'address':address,'mail':mail})
    











