# Generated by Django 3.2.3 on 2021-05-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_alter_book_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(help_text='Если нет даты, то заполняется автоматически', null=True, verbose_name='Дата'),
        ),
    ]
