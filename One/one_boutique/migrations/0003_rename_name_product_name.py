# Generated by Django 4.2.20 on 2025-03-19 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('one_boutique', '0002_rename_catogory_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Name',
            new_name='name',
        ),
    ]
