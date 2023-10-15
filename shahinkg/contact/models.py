from django.db import models


class tamasbama(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    message = models.TextField(max_length=100)
