# Generated by Django 5.2.1 on 2025-07-21 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rf_dispatch', '0005_bin_shelves'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bin',
            name='existing_quantity',
        ),
    ]
