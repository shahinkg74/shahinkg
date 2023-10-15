from django.db import models


class HeaderTitle(models.Model):
     title = models.CharField('title', max_length=70)
    


def __str__(self):
     return self.title