# Generated by Django 4.1 on 2022-10-21 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_like_eventid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='eventId',
        ),
    ]
