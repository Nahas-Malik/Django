from django.db import models

from django.db import models

# A primary model
class Car(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.brand} {self.name}"

# A related model using a OneToOneField
class Engine(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, primary_key=True)
    horsepower = models.IntegerField()

    def __str__(self):
        return f"Engine for {self.car.name}"
