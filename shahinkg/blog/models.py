from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created = models.DateTimeField()





