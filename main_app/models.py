from email.policy import default
from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

FUN_RATING = (
  ('1','Not Fun'),
  ('2','Kinda Fun'),
  ('3','Very Fun'),
)

class Builder(models.Model):
  name = models.CharField(max_length=50)
  build_date = models.DateField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('builders_detail', kwargs={'pk': self.id})


class Lego(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  pieces = models.IntegerField()
  cost = models.IntegerField()
  store_page = models.CharField(max_length=200)
  set_id = models.IntegerField()
  owned = models.BooleanField(default=False)
  
  builders = models.ManyToManyField(Builder)

  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'lego_id': self.id})


class Building(models.Model):
  date = models.DateField('Building Date')
  rating = models.CharField(
    max_length=1,
    choices=FUN_RATING,
    default=FUN_RATING[1][0]
  )
  lego = models.ForeignKey(
    Lego,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f'{self.get_rating_display()} on {self.date}'

  class Meta:
    ordering = ['-date']