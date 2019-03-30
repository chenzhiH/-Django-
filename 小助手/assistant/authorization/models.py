from django.db import models

# Create your models here.

class User(models.Model):
    open_id=models.CharField(max_length=32,unique=True)
    nickname=models.CharField(max_length=356)
    focus_cities=models.TextField(default='[]')
    focus_constellations=models.TextField(default='[]')
    focus_stock=models.TextField(default='[]')

class Eshi(models.Model):
    focus_stock = models.TextField(default=[])