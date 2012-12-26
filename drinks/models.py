from django.db import models

# Create your models here.
class Drink(models.Model):
  """Models an Individual Drink"""
  name = models.CharField(max_length=200)
  alcohol = models.CharField(max_length=200)
  url = models.CharField(max_length=2000)
  def __unicode__(self):
  		return self.name