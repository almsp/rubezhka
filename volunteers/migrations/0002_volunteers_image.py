# Generated by Django 4.2 on 2023-04-19 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteers',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
