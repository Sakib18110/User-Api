from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    contact = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile', blank=True)

    def __str__(self):
        return self.name


class UserHobby(models.Model):
    hobby = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_hobby', blank=True)

    def __str__(self):
        return self.hobby


class UserAddress(models.Model):
    address = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_address', blank=True)

    def __str__(self):
        return self.address
    