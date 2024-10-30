# models.py
from django.db import models

class Applicant(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('denied', 'Denied'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    national_id = models.FileField(upload_to='national_ids/')
    degree_or_diploma = models.FileField(upload_to='degrees/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"