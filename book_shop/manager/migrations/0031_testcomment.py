# Generated by Django 3.2.3 on 2021-06-07 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0030_testtable'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.testtable')),
            ],
        ),
    ]
