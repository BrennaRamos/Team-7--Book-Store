from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profilePic = models.ImageField(default='default.jpg',upload_to='profile_pics')
    address = models.CharField(default='',max_length=100)
    city = models.CharField(default='',max_length=50)
    state = models.CharField(default='',max_length=2)
    zipCode = models.CharField(default='',max_length=5)

    def __str__(self):
        return f'{self.user.username} Profile'

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cardNumber = models.BigIntegerField()
    expDate = models.DateField()
    cvc = models.IntegerField()
    

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(default='',max_length=100)
    city = models.CharField(default='',max_length=50)
    state = models.CharField(default='',max_length=2)
    zipCode = models.CharField(default='',max_length=5)