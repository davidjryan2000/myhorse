from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Horse(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    breed = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    sire = models.CharField(max_length=100)
    dam = models.CharField(max_length=100)
    image = models.ImageField(upload_to='horse_images',
                            default='media/default.png')
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User)
   

    def __str__(self):
        return self.name