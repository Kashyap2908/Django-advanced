from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import Student

# Create your views here.
# @login_required
def home(req):
    ob=Student.objects.all()
    return render(req,'home.html',{'ob':ob})

def user_login(req):
    if req.method=='POST':
        form=AuthenticationForm(req,data=req.POST)
        if form.is_valid():
            login(req,form.get_user())
            return redirect('home')
    else:
        form=AuthenticationForm()
    return render(req,'login.html',{'form':form})

def user_logout(req):
    logout(req)
    return redirect('login')

def add_student(req):
    if req.method=='POST':
        name=req.POST.get('name')
        roll=req.POST.get('roll')
        enroll=req.POST.get('enroll')
        title=req.POST.get('title')
        dob=req.POST.get('dob')
        Student.objects.create(name=name,roll=roll,enroll=enroll,title=title,dob=dob)
    return render(req,'add.html')

def edit_student(req,id):
    if req.method=='POST':
        d=get_object_or_404(Student,id=id)
        d.name=req.POST.get('name')
        d.roll=req.POST.get('roll')
        d.enroll=req.POST.get('enroll')
        d.dob=req.POST.get('dob')
        d.title=req.POST.get('title')
        d.save()
        return redirect('home')
    else:
        d=get_object_or_404(Student,id=id)
    return render(req,'edit.html',{'d':d})

def delete_student(req,id):
    get_object_or_404(Student,id=id).delete()
    return redirect('home')