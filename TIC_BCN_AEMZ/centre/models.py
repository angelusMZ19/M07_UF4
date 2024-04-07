from django.db import models

# Create your models here.
# # 
rol_ = (
    ('student', 'student'),
    ('professor', 'professor'),
)

tutor_ = (
    ('T', 'true'),
    ('F', 'false'),
)
class Student(models.Model):
    nom= models.CharField(max_length=35)
    surname1= models.CharField(max_length=40)
    surname2= models.CharField(max_length=40)
    email= models.CharField(max_length=55)
    course= models.CharField(max_length=25)
    moduls= models.CharField(max_length=50)
    rol= models.CharField(max_length=25,  choices=rol_)

class Professor(models.Model):
    nom= models.CharField(max_length=35)
    surname1= models.CharField(max_length=40)
    surname2= models.CharField(max_length=40)
    email= models.CharField(max_length=55)
    course= models.CharField(max_length=25)
    moduls= models.CharField(max_length=50)
    tutor=models.CharField(max_length=2, choices=tutor_)
    rol= models.CharField(max_length=25,  choices=rol_)