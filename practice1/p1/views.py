from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .forms import StudentForm

# Create your views here.

def show_students(req):
    students=Student.objects.all()
    return render(req,'show.html',{'students':students})

def add_student(req):
    if req.method=='POST':
        form=StudentForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form=StudentForm()
    
    return render(req, 'add.html', {'form':form})

def edit_student(req,id):
    student=get_object_or_404(Student, id=id)
    
    ### ready-made form

    # if req.method=='POST':
    #     form=StudentForm(req.POST, instance=student)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('show')
    # else:  
    #     form=StudentForm(instance=student)
    # return render(req, 'edit.html', {'form':form})


    ### manual form
    
    if req.method=='POST':
        student.name=req.POST.get('name')
        student.roll_no=req.POST.get('roll')
        student.city=req.POST.get('city')
        student.save()
        return redirect('show')
    
    return render(req, 'edit.html', {'student':student})

def delete_student(req,id):
    student=get_object_or_404(Student,id=id)
    if req.method=='POST':
        student.delete()
        return redirect('show')
    
    return render(req,'delete.html',{'student':student})