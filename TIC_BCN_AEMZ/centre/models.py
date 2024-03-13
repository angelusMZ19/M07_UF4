from django.db import models

# Create your models here.
# 
class User (models.Model):
    nom= models.CharField(max_lengtj=30)
    surname= models.CharField(max_lengtj=30)
    email= models.CharField(max_lengtj=50)
    rol= models.CharField(max_lengtj=20)
    course= models.CharField(max_lengtj=20)
