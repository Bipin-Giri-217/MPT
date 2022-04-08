from email import message
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib.auth import logout


def logout(request):
    # logout(request)
    auth.logout(request)
    return redirect('/')

# Create your views here.
def user(request):
    if request.method == 'POST':
        fname= request.POST['name']
        Lname= request.POST['Lname']
        username= request.POST['username']
        #department= request.POST['department']
        phone= request.POST['phone']
        email= request.POST['email']
        email1= request.POST['email1']
        password1= request.POST['password1']
        password2= request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken")
                return render(request, 'register.html')
                


            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")
                return render(request, 'register.html')

            else: 
                user= User.objects.create_user(username=username, password= password1, first_name=fname, last_name=Lname, email=email)
                user.save()
                return render(request, 'login-page.html')
 
        else: 
            messages.info(request, "Check Password")

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        # if user is not None:
        if user:
            auth.login(request, user)
            if request.user.is_staff:
                return redirect('/facultydashboard')
                # return render(request, 'faculty-dashboard.html')

            else:
                # return render(request, 'student-dashboard.html')
                return redirect('/studentdashboard')
        
        else:
            messages.info(request, "Check your cerdentials")
            return render(request, 'login-page.html')

    else: 
        return render(request, 'login-page.html')