from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def home(req):
    return redirect('login')
def dashboard(req):
    if req.user.is_authenticated:
        return render(req,'dashboard.html',{'auth':True,'user':req.user})
    else:
        return render(req,'dashboard.html',{'auth':False})

def user_signup(req):
    if req.method=='POST':
        form=UserCreationForm(req.POST)
        if form.is_valid():
            user=form.save()
            login(req,user)
            return redirect('dashboard')
    else:
        form=UserCreationForm()
    return render(req,'signup.html',{'form':form})

def user_login(req):
    if req.method=='POST':
        form=AuthenticationForm(req,data=req.POST)
        if form.is_valid():
            user=form.get_user()
            login(req,user)
            return redirect('dashboard')
    else:
        form=AuthenticationForm()
    return render(req,'login.html',{'form':form})

def user_logout(req):
    logout(req)
    return render(req,'logout.html')