from django.db import models

class Services(models.Model):
    nume = models.CharField(max_length=255)
    pret = models.DecimalField(max_digits=5, decimal_places=2)
