from django.db import models

from django.core.validators import RegexValidator

# Define a validator for the phone number
phone_validator = RegexValidator(regex=r'^\d{10}$', message="Phone number must be 10 digits.")

# Create your models here.

class Departments(models.Model):
    dept_name=models.CharField(max_length=50)
    no_of_doctors=models.PositiveIntegerField(default=0)
    description = models.TextField(default="We have skilled doctors")
    phoneno = models.CharField(max_length=10, validators=[phone_validator], default='0000000000')
    def __str__(self):
        return "{}".format(self.dname)