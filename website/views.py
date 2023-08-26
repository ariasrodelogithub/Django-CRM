from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    #check to see loggin in
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged Succes Full")
            return redirect('home')
        else: 
            messages.success(request, "There Was An Error In, Please Try Again")
            return redirect('home')
    
    return render(request, 'home.html', {})


def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out")
    return redirect('home')

def register_user(request):
    return render(request, 'register_user.html', {})