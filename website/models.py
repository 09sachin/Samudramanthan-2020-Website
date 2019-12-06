from django.db import models
from django import forms


class events(models.Model):
    Name = models.CharField(max_length=175,default='NULL')
    link = models.CharField(max_length=175,default='NULL')
    logo = models.ImageField(max_length=1000,default='NULL')
    about = models.CharField(max_length=2000)
    rules = models.CharField(max_length=200)
    link2 = models.CharField(max_length=200,default='NULL')
    details = models.CharField(max_length=2000)
    image = models.ImageField(max_length=1000)

    def __str__(self):
        return self.Name


class sponsers(models.Model):
    Name = models.CharField(max_length=175)
    image = models.ImageField(max_length=1000)

    def __str__(self):
        return self.Name

class FeedBack(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=300)
    subject = models.CharField(max_length=400)
    message = models.TextField(max_length=10000)

    def __str__(self):
        return self.name



class RegisterForm(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=300)
    contact = models.CharField(max_length=400)
    college = models.TextField(max_length=1000)
    department = models.TextField(max_length=1000)
    year = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class team(models.Model):
     image = models.ImageField(max_length=1000)
     name = models.CharField(max_length=200)
     fb = models.CharField(max_length=1000)
     post = models.CharField(max_length=100)

     def __str__(self):
         return self.name


class gallery(models.Model):
    image = models.ImageField(max_length=10000)

