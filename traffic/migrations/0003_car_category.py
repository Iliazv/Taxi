# Generated by Django 4.0.1 on 2022-09-29 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0002_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='category',
            field=models.CharField(choices=[('ЭКОНОМ', 'Эконом'), ('КОМФОРТ', 'Комфорт'), ('УНИВЕРСАЛ', 'Универсал')], default='ЭКОНОМ', max_length=50),
        ),
    ]