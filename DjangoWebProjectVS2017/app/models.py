"""
Definition of models.
"""

from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_subject = models.CharField(max_length = 50, default='Sin tema')
    pub_date = models.DateTimeField('date published')
    choices = models.IntegerField(default=0)

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    choice_correcta = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)

class User(models.Model):
    email = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)