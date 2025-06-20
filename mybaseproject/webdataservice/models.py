from django.db import models

# Create your models here.
    
class Emp_data(models.Model):
    title = models.CharField(max_length=10)
    emp_rate = models.CharField(max_length=10)
    
