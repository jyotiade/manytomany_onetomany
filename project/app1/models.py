from django.db import models

# Create your models here.
#===============================many to many=======================

class Fuel(models.Model):
    fuel_name=models.CharField(max_length=50)
    fuel_price=models.IntegerField()
    fuel_density=models.IntegerField()
     
    def __str__(self) :
        return self.fuel_name
        
class Car(models.Model):
    car_name=models.CharField(max_length=50)
    fuel_name=models.ManyToManyField(Fuel)
    car_number=models.IntegerField()
    car_company=models.CharField(max_length=50)

    def __str__(self) :
        return self.car_name