# Generated by Django 4.2.20 on 2025-03-26 11:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one_boutique', '0004_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(12)]),
        ),
    ]
