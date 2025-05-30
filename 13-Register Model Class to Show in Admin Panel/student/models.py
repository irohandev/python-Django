from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=100)


def __str__(self):
    return self.email


class Result(models.Model):
    stu_class = models.CharField(max_length=100)
    marks = models.IntegerField()