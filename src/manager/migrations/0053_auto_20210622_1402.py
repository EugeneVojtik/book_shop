# Generated by Django 3.2.3 on 2021-06-22 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0052_auto_20210622_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketcontent',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_purchase_list', to='manager.shoppingbasketuser'),
        ),
        migrations.AlterUniqueTogether(
            name='shoppingbasketuser',
            unique_together={('user',)},
        ),
    ]
