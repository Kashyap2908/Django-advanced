from django.shortcuts import render,get_object_or_404,redirect
from .models import Student
# Create your views here.
def data(req):
    s=Student.objects.all()
    return render(req,'home.html',{'s':s})

def edit(req,id):
    d=get_object_or_404(Student,id=id)
    if req.method=='POST':
        d.name=req.POST.get('name')
        d.enroll=req.POST.get('enroll')
        d.dob=req.POST.get('dob')
        d.projectTitle=req.POST.get('projectTitle')
        d.save()
        return redirect('home')
    return render(req,'edit.html',{'d':d})

def delete(req,id):
    s=get_object_or_404(Student,id=id)
    s.delete()
    return redirect('home')
