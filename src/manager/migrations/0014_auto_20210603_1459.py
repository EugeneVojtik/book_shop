# Generated by Django 3.2.3 on 2021-06-03 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0013_auto_20210602_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.FloatField(default=5.0, null=True),
        ),
        migrations.AddField(
            model_name='likebookuser',
            name='rate',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
