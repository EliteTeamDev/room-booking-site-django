# Generated by Django 3.2.16 on 2023-04-29 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0007_auto_20230429_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms_added',
            name='room_picture',
            field=models.FileField(default='static/images/rooms/default_room.svg', upload_to='static/images/'),
        ),
    ]