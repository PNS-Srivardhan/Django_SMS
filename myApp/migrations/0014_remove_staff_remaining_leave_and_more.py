# Generated by Django 5.0.3 on 2024-11-24 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0013_alter_staff_basic_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='remaining_leave',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='total_leaves',
        ),
    ]