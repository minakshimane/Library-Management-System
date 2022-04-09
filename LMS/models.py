

from django.db import models

class Admin(models.Model):
    email = models.EmailField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30)

class Book(models.Model):
    ISBN=models.CharField(max_length=30)
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    edition=models.CharField(max_length=50)
    publication=models.CharField(max_length=50)
    admin_email=models.EmailField(max_length=30)

