# Generated by Django 4.1.6 on 2023-03-05 02:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='heartrate',
            field=models.IntegerField(default=60, validators=[django.core.validators.MinValueValidator(limit_value=1), django.core.validators.MaxLengthValidator(limit_value=300)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0), django.core.validators.MaxLengthValidator(limit_value=130)]),
        ),
    ]
