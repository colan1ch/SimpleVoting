from django.db import models
from django.contrib.auth.models import User


class UserSettings(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)


class Voting(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=300)
    type = models.SmallIntegerField()  # вид голосования 1 - radiobutton 2 - checkbox
    options = models.TextField()  # json массив вариантов ответа
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
