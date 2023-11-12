# Generated by Django 3.2.12 on 2023-10-06 06:01

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import main_config.tools
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='description')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='shop.category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('code', models.PositiveSmallIntegerField(default=0, unique=True, verbose_name='code')),
            ],
            options={
                'verbose_name': 'paymwent method',
                'verbose_name_plural': 'payment methods',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create date')),
                ('modify_date', models.DateTimeField(auto_now=True, null=True, verbose_name='modify date')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('image', models.ImageField(upload_to=main_config.tools.UploadToPathAndRename('products'), verbose_name='product image')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='description')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='price')),
                ('view', models.PositiveIntegerField(default=0, verbose_name='view')),
                ('weight', models.PositiveIntegerField(default=0, help_text='input value as Grams', verbose_name='weight')),
                ('count', models.PositiveIntegerField(default=100, verbose_name='count')),
                ('is_featured', models.BooleanField(default=False, verbose_name='is featured')),
                ('min_purchase', models.PositiveIntegerField(default=0, verbose_name='minimum purchase')),
                ('max_purchase', models.PositiveIntegerField(default=100, verbose_name='maximum purchase')),
                ('has_value_added_tax', models.BooleanField(default=True, verbose_name='has value added tax')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.brand', verbose_name='brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='create date')),
                ('modify_date', models.DateTimeField(auto_now=True, null=True, verbose_name='modify date')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='title')),
                ('site_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='site title')),
                ('site_icon', models.ImageField(upload_to=main_config.tools.UploadToPathAndRename('setting'), verbose_name='site icon')),
                ('site_logo', models.ImageField(upload_to=main_config.tools.UploadToPathAndRename('setting'), verbose_name='site logo')),
                ('contact_us', ckeditor.fields.RichTextField()),
                ('product_finishing_alert', models.PositiveIntegerField(default=10, verbose_name='product finishing alert')),
                ('value_added_tax_percent', models.PositiveIntegerField(default=9, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='value added tax percent')),
            ],
            options={
                'verbose_name': 'settings',
                'verbose_name_plural': 'settings',
            },
        ),
        migrations.CreateModel(
            name='ShippingMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('code', models.PositiveSmallIntegerField(default=0, unique=True, verbose_name='code')),
                ('payment_methods', models.ManyToManyField(to='shop.PaymentMethod', verbose_name='payment methods')),
            ],
            options={
                'verbose_name': 'shipping method',
                'verbose_name_plural': 'shipping methods',
            },
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=200, verbose_name='option')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'product option',
                'verbose_name_plural': 'product options',
            },
        ),
        migrations.CreateModel(
            name='ProductMonetaryOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=200, verbose_name='option')),
                ('price', models.PositiveIntegerField(default=0, help_text='Toman', verbose_name='price')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'product monetary option',
                'verbose_name_plural': 'product monetary options',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=main_config.tools.UploadToPathAndRename('products'), verbose_name='product image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'product image',
                'verbose_name_plural': 'product images',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='shipping_methods',
            field=models.ManyToManyField(to='shop.ShippingMethod', verbose_name='shipping merthods'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('title', 'category'), ('title', 'brand')},
        ),
    ]