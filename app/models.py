from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Developer(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=20)
    release_date = models.DateTimeField('Release date')
    price = models.IntegerField()
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    


