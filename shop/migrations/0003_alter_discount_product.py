# Generated by Django 3.2.12 on 2023-10-06 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='product'),
        ),
    ]