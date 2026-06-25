from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField()
    enroll=models.CharField()
    dob=models.DateField()
    projectTitle=models.CharField()

    def __str__(self):
        return self.name