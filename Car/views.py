from django.http import HttpResponse
from django.shortcuts import render
from Car.models import Registeration
# Create your views here.

def home(request):
    # return HttpResponse("This is car module created by Yash Lade")
    return render(request,'index.html')  #will load html pages

def signup(request):
    return render(request,'signup.html',{})

def register(request):
    if request.method=="POST":
        registeration=Registeration()
        fusername =request.POST.get('username')
        fnumber =request.POST.get('number')
        femail =request.POST.get('email')
        fpassword =request.POST.get('password')
        registeration.username=fusername
        registeration.number=fnumber
        registeration.email=femail
        registeration.password=fpassword
        registeration.save()
        return HttpResponse("User Successfully Regsitered")
    return render(request,'register.html',{})
