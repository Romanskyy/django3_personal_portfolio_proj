from django.db import models

# Create your models here.
# Starting create a blog from here


class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
