from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from digiTech.choice import *


# Create your models here.
class Person(models.Model):
    user = models.OneToOneField(User)
    school = models.CharField(max_length=40, default='', blank=True)
    isTeacher = models.BooleanField(default=False)
    location = models.CharField(max_length=10, choices=PLACE_CHOICES, default="0")

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username
