from django.db import models

# Create your models here.

class it_emp(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.IntegerField(max_length=100)
    desk_no = models.CharField(max_length=100)
    sytem_op_sy = models.CharField(max_length=100)
    age = models.IntegerField(max_length=100)
    wing = models.CharField(max_length=100)
    floor = models.CharField(max_length=100)

