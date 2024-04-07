from django.db import models

# Create your models here.
class Registeration(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=10)
    password = models.CharField(max_length=100)