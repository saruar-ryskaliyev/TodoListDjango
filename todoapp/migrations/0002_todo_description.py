# Generated by Django 5.0 on 2024-01-30 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
