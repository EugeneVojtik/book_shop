# Generated by Django 3.2.3 on 2021-06-05 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0022_auto_20210605_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(auto_created=True, null=True, unique=True),
        ),
    ]
