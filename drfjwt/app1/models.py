from django.db import models

# Create your models here.

class Emp(models.Model):
    name=models.CharField()
    age=models.IntegerField()
    position=models.CharField()

    def __str__ (self):
        return self.name