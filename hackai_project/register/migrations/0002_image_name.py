# Generated by Django 4.2.10 on 2024-02-18 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='Name',
            field=models.CharField(default='New File', max_length=25),
        ),
    ]
