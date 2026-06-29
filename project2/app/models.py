from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField()
    roll=models.IntegerField()
    enroll=models.CharField()
    title=models.CharField()
    dob=models.DateField()

    def __str__(self):
        return self.name