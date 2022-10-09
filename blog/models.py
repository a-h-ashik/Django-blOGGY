from django.db import models
import datetime
class Post(models.Model):
  user_name = models.CharField(blank=False, max_length=100)
  tittle = models.CharField(blank=False, max_length= 150)
  description = models.TextField(blank=False)
  date = models.DateField(blank=True)