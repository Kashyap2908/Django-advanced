from django.db import models

# Create your models here.
class Company(models.Model):
    Cname=models.CharField()
    dest=models.CharField()

    def __str__(self):
        return self.Cname
class Employee(models.Model):
    Ename=models.CharField()
    email=models.EmailField()
    company=models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return self.Ename