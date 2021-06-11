# Generated by Django 3.2.3 on 2021-06-10 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0042_auto_20210610_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likebookuser',
            name='tmp_book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tmp_book_likes', to='manager.tmpbook'),
        ),
        migrations.AlterUniqueTogether(
            name='likebookuser',
            unique_together={('tmp_book', 'user')},
        ),
        migrations.RemoveField(
            model_name='likebookuser',
            name='book',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
