from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Institution(models.Model):
    ORG_TYPES = {
        ('FOUND', 'fundacja'),
        ('ORG', 'organizacja pozarządowa'),
        ('LOCAL', 'zbiórka lokalna'),
    }
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=1000)
    type = models.CharField(choices=ORG_TYPES, max_length=5, default='FOUND')
    categories = models.ManyToManyField(Category)

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=12)
    city = models.CharField(max_length=24)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.CharField(max_length=128)
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.PROTECT)