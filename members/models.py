from django.db import models

# Create your models here.


class Members(models.Model):
  Cryptocurrency = models.CharField(max_length=255)
  Amount = models.CharField(max_length=255)
