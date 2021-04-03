# Generated by Django 3.1.7 on 2021-03-31 16:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingoodhands', '0004_auto_20210325_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='donation',
            name='address',
            field=models.CharField(max_length=128, verbose_name='Ulica'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='city',
            field=models.CharField(max_length=24, verbose_name='Miasto'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='phone_number',
            field=models.CharField(max_length=12, verbose_name='Numer telefonu'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='pick_up_comment',
            field=models.CharField(max_length=128, verbose_name='Uwagi dla kuriera'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='pick_up_date',
            field=models.DateField(verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='pick_up_time',
            field=models.TimeField(verbose_name='Godzina'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(60)], verbose_name='Liczba 60l worków: '),
        ),
        migrations.AlterField(
            model_name='donation',
            name='zip_code',
            field=models.CharField(max_length=6, verbose_name='Kod pocztowy'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='type',
            field=models.CharField(choices=[('FOUND', 'fundacja'), ('ORG', 'organizacja pozarządowa'), ('LOCAL', 'zbiórka lokalna')], default='FOUND', max_length=5),
        ),
    ]