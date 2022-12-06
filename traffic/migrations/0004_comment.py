# Generated by Django 4.0.1 on 2022-09-30 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0003_car_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=1800)),
                ('date', models.DateTimeField(verbose_name='Published')),
            ],
        ),
    ]
