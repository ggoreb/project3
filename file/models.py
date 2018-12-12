from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50)
    file = models.CharField(max_length=200)
