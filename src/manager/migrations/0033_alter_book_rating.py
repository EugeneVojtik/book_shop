# Generated by Django 3.2.3 on 2021-06-08 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0032_alter_testcomment_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
