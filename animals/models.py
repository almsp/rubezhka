from django.db import models
from volunteers.models import Volunteers
from django.contrib.auth.models import User

class AnimalsCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Animals(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    breed = models.CharField(max_length=30)
    category = models.ForeignKey(AnimalsCategory, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField(default=0, blank=True, null=True)
    age = models.IntegerField(default=0, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    colour = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.name


class Pay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    number = models.CharField(max_length=16)
