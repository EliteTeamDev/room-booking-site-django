# Generated by Django 3.0.4 on 2020-03-11 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='login',
            new_name='login_data',
        ),
    ]