# Generated by Django 4.1.5 on 2023-01-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0002_remove_event_emotion_remove_event_weather_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='c_date',
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
