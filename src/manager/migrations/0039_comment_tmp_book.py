# Generated by Django 3.2.3 on 2021-06-10 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0038_alter_likebookuser_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='tmp_book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='manager.tmpbook'),
        ),
    ]