from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=80, unique=True)
    visible = models.BooleanField(default=True)
    # manytomany so you can either copy modules or use the exact same one
    # modules = models.ManyToManyField
    key = models.CharField(max_length=20, default=None, null=True)
