from django.db import models
from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models.signals import post_save

class User(models.Model):
    user_name = models.CharField(max_length=20, primary_key = True)
    name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=10)
    email_id = models.EmailField()
    residence = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.user_name
