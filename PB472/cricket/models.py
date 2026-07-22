from django.db import models

# Create your models here.
class Player(models.Model):
    name=models.CharField()
    country=models.CharField()
    batting_style=models.CharField()
    bowling_style=models.CharField()
    age=models.IntegerField()
    runs=models.IntegerField()
    wickets=models.IntegerField()

    def __str__(self):
        return self.name