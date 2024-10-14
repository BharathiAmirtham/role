from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone

class Person(models.Model):
    name = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30)
    department = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.name

class Role(models.Model):
    ADMIN = 'admin'
    TEACHER = 'teacher'
    STUDENT = 'student'

    ROLE_CHOICES = [
        (ADMIN, ADMIN),
        (TEACHER, TEACHER),
        (STUDENT, STUDENT),
    ]

    role = models.CharField( 
        max_length = 30, 
        choices = ROLE_CHOICES, 
        default = '1',null=True, blank=True
        ) 


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name='profile')
    role=models.ForeignKey(Role, on_delete=models.CASCADE,null=True, blank=True)
    city = models.CharField(max_length = 50, blank = True, null = True)
    phone_no = models.IntegerField(blank = True, null = True)
    biometric_id = models.IntegerField(blank = True, null = True)
    roll_no = models.IntegerField(blank = True, null = True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

