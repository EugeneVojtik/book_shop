# Generated by Django 3.2.3 on 2021-06-10 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0036_auto_20210610_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='tmpbook',
            name='id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
