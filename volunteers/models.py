from django.db import models
from django.contrib.auth.models import User

class Volunteers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    age = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return self.email