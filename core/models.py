from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Library(models.Model):
    name = models.TextField()
    adress = models.TextField()

    def getAdress(self):
        return self.adress

    def __str__(self):
        return self.name

