# Generated by Django 4.2 on 2023-04-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonDRF', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorDet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=255)),
                ('age', models.IntegerField(default=1)),
            ],
        ),
    ]
