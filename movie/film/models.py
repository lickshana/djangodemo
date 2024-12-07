from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    language = models.CharField(max_length=20)
    year = models.IntegerField()
    image = models.ImageField(upload_to="image")


def _str_(self):
    return self.title