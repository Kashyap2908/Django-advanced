from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField()
    roll_no=models.IntegerField()
    city=models.CharField()

    def __str__(self):
        return self.name