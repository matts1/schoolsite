from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=80, unique=True)
    # manytomany so you can either copy modules or use the exact same one
    # modules = models.ManyToManyField
