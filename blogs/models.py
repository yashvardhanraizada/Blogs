from django.db import models
from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import date
from django.utils import timezone

class User(models.Model):
    user_name = models.CharField(max_length=20, primary_key = True)
    name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=10)
    email_id = models.EmailField()
    residence = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.user_name

class Blog(models.Model):
    timestamp = models.DateTimeField(primary_key = True, default=timezone.now)
    publish_status = models.CharField(max_length=8, choices=(('Accepted','Accepted'), ('Rejected', 'Rejected'), ('Pending', 'Pending')), default='Pending')
    title = models.CharField(max_length=20)
    blog_description = models.CharField(max_length=100, default='NA')
    author = models.CharField(max_length=50)
    author_email = models.EmailField(default='NA')
    author_details = models.CharField(max_length=200, default='NA')
    target_stream = models.CharField(max_length=100)
    blog_text = models.TextField(default='NA')
    head_image = models.ImageField(default='NA')
    relevant_links = models.URLField(default='NA')
    def __str__(self):
        return "%s by %s -> %s (%s)" % (self.title, self.author, self.target_stream, self.publish_status)

class Blogger(models.Model):
    blogger_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=20, primary_key = True)
    blogger_since = models.DateField(default=date.today)
    def __str__(self):
        return "%s @ %s" % (self.blogger_name, self.user_name)

class Stream(models.Model):
    stream_id = models.CharField(max_length=30, primary_key = True)
    stream_name = models.CharField(max_length=30)
    stream_description = models.CharField(max_length=100, default='NA')
    stream_owner = models.CharField(max_length=20)
    date_of_launch = models.DateField(default=date.today)
    def __str__(self):
        return "%s @ %s | Owner : %s" % (self.stream_name, self.stream_id, self.stream_owner)
