# Generated by Django 3.1.1 on 2020-10-17 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelpackages', '0005_auto_20201017_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='bpacname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
