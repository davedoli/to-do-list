from django.db import models

# Create your models here.

class Task(models.Model):
    posted_date = models.DateField()