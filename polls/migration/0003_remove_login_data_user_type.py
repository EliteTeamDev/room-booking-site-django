# Generated by Django 3.0.4 on 2020-03-11 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200311_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login_data',
            name='user_type',
        ),
    ]
