from django.shortcuts import render,redirect
from .models import Dep,Student
from io import TextIOWrapper
import csv
from django.http import HttpResponse
# Create your views here.
def home(request):
    
    return render(request,"show.html")

def show_stu(request):
    data=Student.objects.all()
    
    return render(request,"show_stu.html",{"data":data})

def upload_csv(request):
    if request.method == "POST":
        csv_file = request.FILES["csv1_file"]
        file = TextIOWrapper(csv_file.file, encoding="utf-8")
        
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        
        for row in reader:
            name = row[0]
            eno = row[1]
            email = row[2]
            department_name = row[3]  # This is a string (e.g., 'Computer Science')
            
            # 1. Safely find or create the Department model instance first
            dept_instance, created = Dep.objects.get_or_create(
                dept_name=department_name,
                defaults={'hod_name': 'dhruv'}  # Default HOD name if creating a new dept
            )
            
            # 2. Pass the saved model instance into your ForeignKey field
            Student.objects.create(
                name=name,
                email=email,
                eno=eno,
                deparment=dept_instance  # Asserts the object instance, not a string
            )
            
        return redirect("show_stu")
        
    return render(request, "upload_csv.html")
