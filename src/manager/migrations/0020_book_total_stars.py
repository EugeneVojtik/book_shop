# Generated by Django 3.2.3 on 2021-06-04 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0019_alter_likebookuser_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_stars',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
