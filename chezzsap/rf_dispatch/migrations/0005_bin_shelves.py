# Generated by Django 5.2.1 on 2025-07-21 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rf_dispatch', '0004_bin'),
    ]

    operations = [
        migrations.AddField(
            model_name='bin',
            name='shelves',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
