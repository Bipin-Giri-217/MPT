from email import message
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib.auth import logout
from accounts.models import User

def login(request):
    logout(request)
    if request.method == 'POST':
        email= request.POST['email']
        password= request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user:
            if user.is_active:
                auth.login(request, user)
                if request.user.is_superuser ==True:
                    return redirect('/AdminPage')

                elif request.user.is_staff==True:
                    return redirect('/facultydashboard/'+str(user.usr_id),pk=user.usr_id)
                
                else:
                    return redirect('/studentdashboard/'+str(user.usr_id),pk=user.usr_id)
            else:
                messages.info(request, 'Activate Your Account First then try to login...')
        
        else:
            messages.info(request, "Check your cerdentials")
            return render(request, 'Login/login-page.html')

    else: 
        return render(request, 'Login/login-page.html')

def cPassword(request):
    context = {}
    return render(request,'change-password.html',context);