from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"