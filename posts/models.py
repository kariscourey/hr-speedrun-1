from django.db import models

# Create your models here.

# ORM - object relational mapper

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
