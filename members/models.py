from django.db import models

# Create your models here.
class Member(models.Model):
    member_id = models.CharField(max_length=10)
    member_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    dob = models.DateField(max_length=50)
    gender = models.CharField(max_length=50)
    stauts = models.CharField(max_length=2)

    def __str__(self):
        return self.member_name