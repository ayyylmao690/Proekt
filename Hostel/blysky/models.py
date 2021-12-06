from django.db import models
class Country(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Hotel(models.Model):
    town = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
# Create your models here
