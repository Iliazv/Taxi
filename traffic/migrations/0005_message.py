# Generated by Django 4.0.1 on 2022-10-02 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=3000)),
                ('date', models.DateTimeField(verbose_name='Send')),
            ],
        ),
    ]
