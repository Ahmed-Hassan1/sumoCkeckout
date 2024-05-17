from django.db import models

# Create your models here.

class Sumo(models.Model):
    upload=models.FileField(null=True,blank=True)