from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    inventory = models.IntegerField()

    def __str__(self):
        return self.name

# Create your models here.
