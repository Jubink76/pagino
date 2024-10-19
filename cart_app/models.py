
from django.db import models
from log_reg_app.models import UserTable
# Create your models here.
class CartTable(models.Model):
    quantity = models.IntegerField()
    added_time = models.TimeField()
    is_whishlisted = models.BooleanField()

    user = models.OneToOneField('log_reg_app.UserTable', on_delete=models.CASCADE)

    class Meta:
        db_table = 'table_cart'
