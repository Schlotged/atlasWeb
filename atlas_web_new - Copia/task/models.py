from typing import Any
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Setor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Create your models here.
class Task(models.Model):
    
    name_task = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.name_task