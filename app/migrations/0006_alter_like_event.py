# Generated by Django 4.1 on 2022-10-21 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_like_eventid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.event'),
        ),
    ]
