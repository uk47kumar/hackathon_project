
from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    subject = models.CharField(max_length=12)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class SIGNUP(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    password = models.CharField(max_length=25)
    confirmedpassword = models.CharField(max_length=25)
    otp = models.IntegerField(blank=True, null=True)
    # def save(self,*args,**kwargs/)

    def __str__(self):
        return self.name


class LOGIN(models.Model):
    email = models.EmailField(max_length=122)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.email


class APPOINTMENT(models.Model):
    name = models.CharField(max_length=122)
    phonenumber = models.CharField(max_length=12)
    drname = models.CharField(max_length=122)
    department = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    message = models.TextField()

    def __str__(self):
        return self.name

