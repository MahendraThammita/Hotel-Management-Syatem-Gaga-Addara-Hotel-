# Generated by Django 3.1.1 on 2020-09-23 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='attraction',
            fields=[
                ('attractionID', models.IntegerField(primary_key=True, serialize=False)),
                ('img', models.CharField(max_length=1000)),
                ('Discription', models.CharField(max_length=350)),
                ('distance', models.FloatField()),
            ],
            options={
                'db_table': 'attraction',
            },
        ),
        migrations.CreateModel(
            name='Customer_Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cusId', models.CharField(max_length=10)),
                ('feedbackId', models.IntegerField()),
            ],
            options={
                'db_table': 'Customer_Feed',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedbackId', models.IntegerField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=20)),
                ('rate', models.IntegerField()),
                ('description', models.CharField(max_length=250)),
                ('ansDescription', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'Feedback',
            },
        ),
    ]
