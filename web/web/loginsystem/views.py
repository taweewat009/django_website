from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST["pass"]
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            fname = user.first_name
            return render(request,'index.html',{'fname':fname})
        else:
            messages.info(request,"ไม่พบข้อมูลบัญชีผู้ใช้")
            return redirect("login")
    
    return render(request,"loginsystem/signin.html")
        
    

def logout(request):
    auth.logout(request)
    return redirect("index")