# Generated by Django 3.2.3 on 2021-06-25 11:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0056_usersbooks'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usersbooks',
            unique_together={('book', 'user')},
        ),
    ]
