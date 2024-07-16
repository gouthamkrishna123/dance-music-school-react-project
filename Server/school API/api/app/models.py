from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     # Add any additional user fields you need, e.g., phone_number, bio
#     pass

# Create your models here.

class contact(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=50)
    message=models.CharField(max_length=100)

class register(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    age=models.CharField(max_length=3)
    date_of_birth = models.DateField()
    gender= models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pincode=models.CharField(max_length=6)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=30)

# class Booking(models.Model):
#     country = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     course=models.CharField(max_length=20)
#     location = models.CharField(max_length=100)
#     batches = models.CharField(max_length=100)
#     fees = models.CharField(max_length=100)

class Book(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    course=models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    batches = models.CharField(max_length=100)
    fees = models.CharField(max_length=100)

    