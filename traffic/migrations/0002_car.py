# Generated by Django 4.0.1 on 2022-09-29 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('photo', models.ImageField(blank=True, upload_to='expert_images/')),
                ('year', models.IntegerField()),
            ],
        ),
    ]
