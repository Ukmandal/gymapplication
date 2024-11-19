import datetime
from django.db import models


class Manager(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13, blank=True)
    designation = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    date_of_birth = models.DateField(
        default=datetime.date.today, blank=True, null=True)
    gender = models.CharField(max_length=10)
    status = models.CharField(max_length=10)

    def __str__(self):
         return f'Manager: {self.first_name} {self.last_name}'

# return f'Student: {self.first_name} {self.last_name}'