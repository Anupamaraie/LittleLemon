# Generated by Django 4.2 on 2023-04-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonDRF', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='inventory',
            field=models.IntegerField(default=1),
        ),
    ]
