from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(req):
    if(req.method == 'POST'):
        #the user wants to signup
        if req.POST['password1'] == req.POST['password2']:
            try: 
                user = User.objects.get(username=req.POST['username'])
                return render(req, 'accounts/signup.html', {'error': "Username is already present"})
            except User.DoesNotExist:
                user = User.objects.create_user(req.POST['username'], password=req.POST['password1'])
                auth.login(req, user)
                return redirect('home')
        else:
            return render(req, 'accounts/signup.html', {'error': "Passwords must match"})
    else:
        return render(req,'accounts/signup.html')


def login(req):
    if(req.method == 'POST'):
        user = auth.authenticate(username=req.POST['username'], password=req.POST['password'])
        if user is not None:
            auth.login(req, user)
            return redirect('home')
        else:
            return render(req, 'accounts/login.html', {"error": "Username or password is incorrect"})
    else:
        return render(req, 'accounts/login.html')


def logout(req):
    if(req.method == 'POST'):
        auth.logout(req)
        return redirect('home')


    #TODO need to route to homepage
    return render(req, 'accounts/signup.html')
