from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField

from hms.models import Departments

# Define a validator for the phone number
phone_validator = RegexValidator(regex=r'^\d{10}$', message="Phone number must be 10 digits.")
# Create your models here.


class User(AbstractUser):
    ROLE_CHOICES = (
        ('doctor', 'doctor'),
        ('patient', 'patient'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient')
    profile_pic = CloudinaryField("Image", overwrite=True, resource_type="image", use_filename=True, unique_filename=True,
    transformation={"quality": 'auto:low', 'width':300, 'height': 300, 'crop': "scale",},
    format="jpeg")
    address = models.CharField(max_length=40)
    phoneno = models.CharField(max_length=10, validators=[phone_validator], default='0000000000')

    def __str__(self):
        return f"{self.username} ({self.role})"

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    department= models.ForeignKey(Departments, on_delete=models.CASCADE)
    status=models.BooleanField(default=False) #whether he/she is in cabin or not
    experience = models.PositiveIntegerField(default=0)
    @property
    def get_name(self):
        return "{} {}".format(self.user.first_name,self.user.last_name)
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.username,self.department)
    
    
# class Patient(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
    
#     @property
#     def get_name(self):
#         return self.user.first_name+" "+self.user.last_name
#     @property
#     def get_id(self):
#         return self.user.id
#     def __str__(self):
#         return "{}".format(self.user.first_name+''+self.user.last_name)
    