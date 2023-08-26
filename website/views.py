from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SingUpForm, AddRecordForm
from .models import Record

def home(request):
    records = Record.objects.all()

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
    
    return render(request, 'home.html', {'records': records})



def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticated
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You Have Been Logged Succes Full")
                return redirect('home')
    else:
        form = SingUpForm()
        return render(request, 'register_user.html', {'form': form})

    return render(request, 'register_user.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer': customer_record})
    else:
        messages.success(request, "You Must Be In TO View That Page")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        customer_record.delete()
        messages.success(request, "Delete Record SuccesFully")
        return redirect('home')
    else:
        messages.success(request, " You Must Be Logged To Do That ")
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added")
                return redirect('home')

        return render(request, 'add_customer.html', {'form': form})
    else:
        messages.success(request, " You Must Be Logged To Do That ")
        return redirect('home')
    

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated")
            return redirect('home')
        return render(request, 'update_customer.html', {'form': form})
    else:
        messages.success(request, " You Must Be Logged To Do That ")
        return redirect('home')