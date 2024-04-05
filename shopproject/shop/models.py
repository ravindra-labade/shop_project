from django.db import models


class Shop(models.Model):
    shop_name = models.CharField(max_length=20)
    shop_address = models.CharField(max_length=20)
    shop_owner = models.CharField(max_length=20)
    operated_since = models.DateField()
    available_services = models.CharField(max_length=20)
    choice = [('Online', 'ONLINE'), ('Cash', 'CASH')]
    payment_mode = models.CharField(max_length=10, choices=choice)

