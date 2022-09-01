from dataclasses import dataclass
from http.client import OK
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.


def Home_show(request):
    username = str(request.GET.get('name'))
    
    if username == "rohit":
        f = "Done"       
    
    else:
        f ="Wrong Username OR Passwd Call First Rohit you Than log in"
    logger_Data={
        'Name':username,
        # 'submit':input_submit,
        'pp':f
    }
        
   
  
    
            
    # return HttpResponse("wleomchome")
    return render(request, 'index.html',logger_Data)


def About_show(request):
    # return HttpResponse("wleomchome")
    return render(request, 'about.html')


def Info_show(request):
    # return HttpResponse("wleomchome")
    
    
    return render(request, 'info.html')


def Homepress(request):
    # return HttpResponse("wleomchome")
    return HttpResponse( '<a class="btn btn-primary btn btn-dark x-2" href="1" role="button">HomePage</a>')

import time

def EnterPage(request):
  
    # if request.method == 'POST':
    #     input_username = str(request.GET.get('userN'))
    #     input_youfrom = str(request.GET.get('youfN'))
        
        
    # dic ={
    #     'list':[ {'username' :input_username,'userpassword':input_youfrom}],
    # }
        

    return render(request,'log_page.html')




def index(request):
    pass
    