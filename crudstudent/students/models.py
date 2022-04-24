from django.db import models

# Create your models here.

class Student(models.Model):

    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    email = models.EmailField()
    econtact = models.CharField(max_length=15)

    class Meta:
        db_table="ajeet"