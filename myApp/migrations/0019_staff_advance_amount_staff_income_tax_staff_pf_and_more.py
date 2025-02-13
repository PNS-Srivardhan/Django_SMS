# Generated by Django 5.0.3 on 2024-12-13 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0018_staff_remainingleaves'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='advance_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='staff',
            name='income_tax',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='staff',
            name='pf',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='staff',
            name='totalleaves',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]
