from account.models import NewUser
from django.db import models

# Create your models here.

class Sell_flat(models.Model):

    divission = models.CharField(max_length=20, null=True, blank=True)
    district = models.CharField(max_length=20, null=True, blank=True)

    location = models.TextField(max_length=255, null=True, blank=True)
    price = models.BigIntegerField(null=True, blank=True)
    ammount = models.CharField(max_length=50, null=True, blank=True)

    floors_count = models.IntegerField(null=True, blank=True)
    floor_face = models.CharField(null=True, blank=True, max_length=50)

    details = models.TextField(null=True, blank=True)
    flat_image = models.ImageField(upload_to='flat_photos', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)

    def __str__(self):
         return self.location

class Sell_land(models.Model):

    divission = models.CharField(max_length=20, null=True, blank=True)
    district = models.CharField(max_length=20, null=True, blank=True)

    location = models.TextField(max_length=255, null=True, blank=True)
    price = models.BigIntegerField(null=True, blank=True)
    ammount = models.CharField(max_length=50, null=True, blank=True)

    plots_count = models.IntegerField(null=True, blank=True)
    land_type = models.CharField(null=True, blank=True, max_length=50)

    details = models.TextField(null=True, blank=True)
    land_image = models.ImageField(upload_to='land_photos', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)

    def __str__(self):
         return self.location


class OwnerRent(models.Model):
    property_type = models.CharField(max_length=255, null=True, blank=True)
    rent_type = models.CharField(max_length=255, null=True, blank=True)

    division = models.CharField(max_length=20, null=True, blank=True)
    district = models.CharField(max_length=20, null=True, blank=True)

    property_location = models.TextField(max_length=100, null=True, blank=True)
    rent_money = models.IntegerField(null=True, blank=True)
    money_type = models.CharField(max_length=255, null=True, blank=True)

    floor_no = models.CharField(null=True, blank=True, max_length=20)
    floor_face = models.CharField(null=True, blank=True, max_length=50)
    plot_size = models.IntegerField(null=True, blank=True)
    numerical_value_type = models.TextField(max_length=50, null=True, blank=True)
    area_description = models.TextField(max_length=250, null=True, blank=True)
    rent_photo = models.ImageField(upload_to='rent', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user_email = models.EmailField(max_length=200,blank=True, null=True)
    phone_no=models.CharField(max_length=20,null=True, blank=True)

    # def __str__(self):
    #      return self.rent_type
