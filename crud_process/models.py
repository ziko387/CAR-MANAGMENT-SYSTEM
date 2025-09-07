from django.db import models


# Create your models here.
class CarItems(models.Model):
    car_name = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_image = models.ImageField(upload_to='images/')
    car_price = models.IntegerField()

    def __str__(self):
        return self.car_name
    
