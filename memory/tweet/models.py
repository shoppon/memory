from django.db import models

class Tweet(models.Model):
    time = models.TimeField()
    content = models.CharField(max_length=1024)
