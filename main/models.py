from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100)


class Voting(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=300)
    type = models.SmallIntegerField()  # вид голосования 1 - radiobutton 2 - checkbox
    options = models.TextField()  # json массив вариантов ответа
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)


class Comment(models.Model):
    text = models.CharField(max_length=100)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    voting = models.ForeignKey(to=Voting, on_delete=models.CASCADE)


class Vote(models.Model):  # при многовыборочном голосовании создаётся несколько штук
    option = models.SmallIntegerField()  # индекс ответа в json массиве
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    voting = models.ForeignKey(to=Voting, on_delete=models.CASCADE)

#со временем будем расширять
