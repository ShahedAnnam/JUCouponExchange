from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    batch = models.IntegerField()
    number = models.CharField(max_length=50)
    message = models.TextField()
    allotedHall = models.CharField(max_length=50)
    desiredHall = models.CharField(max_length=50)

    def __str__(self):
        return self.name

