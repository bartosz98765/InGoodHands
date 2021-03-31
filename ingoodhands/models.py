from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


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

    def __str__(self):
        return f'{self.get_type_display()}: {self.name}'.title()


class Donation(models.Model):
    quantity = models.IntegerField(verbose_name='Liczba 60l worków: ',
                                   validators=[MinValueValidator(1), MaxValueValidator(60)])
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)
    address = models.CharField(max_length=128, verbose_name='Ulica')
    phone_number = models.CharField(max_length=12, verbose_name='Numer telefonu')
    city = models.CharField(max_length=24, verbose_name='Miasto')
    zip_code = models.CharField(max_length=6, verbose_name='Kod pocztowy')
    pick_up_date = models.DateField(verbose_name='Data')
    pick_up_time = models.TimeField(verbose_name='Godzina')
    pick_up_comment = models.CharField(max_length=128, verbose_name='Uwagi dla kuriera')
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.PROTECT)
    is_taken = models.BooleanField(default=False)
