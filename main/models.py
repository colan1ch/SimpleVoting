from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models


class User(AbstractUser):
    status = models.CharField(max_length=255)


class UserSettings(models.Model):
    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE)


class Voting(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=300)
    type = models.SmallIntegerField()  # вид голосования 1 - radiobutton 2 - checkbox
    options = models.TextField()  # json массив вариантов ответа
    user = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL, null=True)
