# Generated by Django 5.0 on 2024-01-30 10:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 30, 10, 35, 7, 371088, tzinfo=datetime.timezone.utc)),
        ),
    ]