# Generated by Django 5.0.3 on 2024-11-24 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0014_remove_staff_remaining_leave_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='remaining_leaves',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='staff',
            name='total_leaves',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
