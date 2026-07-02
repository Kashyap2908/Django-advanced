from django.db import models

# Create your models here.
class Dep(models.Model):
    hod_name=models.CharField()
    dept_name=models.CharField(null=True)
    
    def __str__(self):
        return self.dept_name
    
class Student(models.Model):
    name=models.CharField()
    email=models.CharField()
    eno=models.IntegerField()
    deparment=models.ForeignKey(Dep,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="students/",blank=True,null=True)
    def __str__(self):
        return self.name
    