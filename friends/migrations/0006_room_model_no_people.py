# Generated by Django 3.1.4 on 2020-12-16 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0005_auto_20201215_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='room_model',
            name='no_people',
            field=models.IntegerField(default=0),
        ),
    ]
