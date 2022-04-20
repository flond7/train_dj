from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=True, default='')
    surname = models.CharField(max_length=50, blank=True, default='')
    mail = models.EmailField(max_length=150)
    pw = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default='')
    answerOne = models.TextField(default='')
    answerTwo = models.TextField(default='')
    answerThree = models.TextField(default='')
    correct = models.TextField(default='')
    id_path = models.IntegerField()
    id_video = models.IntegerField()

    class Meta:
        ordering = ['id']

class Result(models.Model):
    id = models.AutoField(primary_key=True)
    correct = models.BooleanField()
    id_question = models.IntegerField()
    id_user = models.IntegerField()  

    class Meta:
        ordering = ['id']