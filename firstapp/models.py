from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    objects = models.Manager()


class Company(models.Model):
    name = models.CharField(max_length=30)


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    price = models.IntegerField()

class Course(models.Model):
    name = models.CharField(max_length=30)

class Student(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course)


class User(models.Model):
    name = models.CharField(max_length=20)


class Account(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key= True)
