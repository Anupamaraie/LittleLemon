# Generated by Django 4.2 on 2023-04-20 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonDRF', '0002_authordet'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authordet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='LittleLemonDRF.authordet'),
        ),
    ]