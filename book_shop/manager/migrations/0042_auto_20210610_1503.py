# Generated by Django 3.2.3 on 2021-06-10 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0041_auto_20210610_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='ну это типа название книги', max_length=50, verbose_name='Наименование')),
                ('date', models.DateTimeField(auto_now_add=True, help_text='Если нет даты, то заполняется автоматически', null=True, verbose_name='Дата')),
                ('description', models.TextField(default='Book description to be added soon', null=True)),
                ('likes', models.PositiveIntegerField(default=0, null=True)),
                ('rating', models.FloatField(default=0.0, null=True)),
                ('total_stars', models.PositiveIntegerField(default=0, null=True)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('authors', models.ManyToManyField(related_name='books', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'книга',
                'verbose_name_plural': 'книги',
            },
        ),
        migrations.AddField(
            model_name='likebookuser',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_likes', to='manager.book'),
        ),
        migrations.AlterUniqueTogether(
            name='likebookuser',
            unique_together={('book', 'user')},
        ),
    ]