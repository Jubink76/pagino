from django.db import models
from log_reg_app.models import UserTable
# Create your models here.

class AddressTable(models.Model):
    name = models.CharField(max_length=256,null=False,blank=False)
    house_name = models.CharField(max_length = 256, null = False, blank= False)
    street_name = models.CharField(max_length= 256)
    city_name = models.CharField(max_length=256)
    state = models.CharField(max_length= 256, null = False, blank=False)
    pincode = models.CharField(max_length= 50, null = False, blank= False)
    email = models.EmailField()
    phone = models.CharField(max_length= 15)

    user = models.ForeignKey('log_reg_app.UserTable', related_name='addresses', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.street_name},{self.city_name}"