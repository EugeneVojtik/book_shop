# Generated by Django 3.2.3 on 2021-06-22 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0051_delete_tableaggregate'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.SmallIntegerField(default=100),
        ),
        migrations.CreateModel(
            name='ShoppingBasketUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_basket', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'id')},
            },
        ),
        migrations.CreateModel(
            name='BasketContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Users_purchase_list', to='manager.shoppingbasketuser')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket', to='manager.book')),
            ],
        ),
    ]