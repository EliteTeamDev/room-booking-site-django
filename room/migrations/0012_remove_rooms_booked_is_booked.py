# Generated by Django 3.2.16 on 2023-04-30 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0011_auto_20230429_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms_booked',
            name='is_booked',
        ),
    ]