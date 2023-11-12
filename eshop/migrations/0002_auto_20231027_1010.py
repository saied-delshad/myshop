# Generated by Django 3.2.12 on 2023-10-27 06:40

import admin_theme.tools
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import eshop.validators
import main_config.tools


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_theme', '0001_initial'),
        ('eshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'برند', 'verbose_name_plural': 'برند ها'},
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'سبد خرید', 'verbose_name_plural': 'سبد های خرید'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'آیتم سبد خرید', 'verbose_name_plural': 'آیتم های سبد خرید'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='discount',
            options={'verbose_name': 'تخفیف', 'verbose_name_plural': 'تخفیفات'},
        ),
        migrations.AlterModelOptions(
            name='discountcode',
            options={'verbose_name': 'کد تخفیف', 'verbose_name_plural': 'کد های تخفیف'},
        ),
        migrations.AlterModelOptions(
            name='paymentmethod',
            options={'verbose_name': 'paymwent method', 'verbose_name_plural': 'روش های پرداخت'},
        ),
        migrations.AlterModelOptions(
            name='paymentstatus',
            options={'ordering': ('code',), 'verbose_name': 'وضعیت پرداخت', 'verbose_name_plural': 'وضعیت های پرداخت'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'تصویر محصول', 'verbose_name_plural': 'تصاویر محصول'},
        ),
        migrations.AlterModelOptions(
            name='productmonetaryoption',
            options={'verbose_name': 'ویژگی پولی محصول', 'verbose_name_plural': 'ویژگی های پولی محصول'},
        ),
        migrations.AlterModelOptions(
            name='productproperty',
            options={'verbose_name': 'ویژگی محصول', 'verbose_name_plural': 'ویژگی های محصول'},
        ),
        migrations.AlterModelOptions(
            name='setting',
            options={'verbose_name': 'تنظیمات', 'verbose_name_plural': 'تنظیمات'},
        ),
        migrations.AlterModelOptions(
            name='shippingcost',
            options={'verbose_name': 'هزینه ارسال', 'verbose_name_plural': 'هزینه های ارسال'},
        ),
        migrations.AlterModelOptions(
            name='shippingmethod',
            options={'verbose_name': 'روش ارسال', 'verbose_name_plural': 'روش های ارسال'},
        ),
        migrations.AlterModelOptions(
            name='shippingstatus',
            options={'ordering': ('code',), 'verbose_name': 'وضعیت ارسال', 'verbose_name_plural': 'وضعیت های ارسال'},
        ),
        migrations.AlterField(
            model_name='brand',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ ویرایش'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='title',
            field=models.CharField(max_length=200, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='discount_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eshop.discountcode', verbose_name='کد تخفیف'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ ویرایش'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.cart', verbose_name='سبد خرید'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='count',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='تعداد'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ ویرایش'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='monetary_option',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eshop.productmonetaryoption', verbose_name='ویژگی پولی محصول'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.product', verbose_name='محصول'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, default='', null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='category',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='سفارش'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ ویرایش'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='percent',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='درصد تخفیف'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='eshop.product', verbose_name='محصول'),
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='code',
            field=models.CharField(default=admin_theme.tools.create_code, max_length=255, unique=True, verbose_name='کد'),
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ ویرایش'),
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='percent',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='درصد تخفیف'),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='code',
            field=models.PositiveSmallIntegerField(default=0, unique=True, verbose_name='کد'),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ ویرایش'),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='title',
            field=models.CharField(max_length=200, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='paymentstatus',
            name='code',
            field=models.PositiveSmallIntegerField(default=0, unique=True, verbose_name='کد'),
        ),
        migrations.AlterField(
            model_name='paymentstatus',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='paymentstatus',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ ویرایش'),
        ),
        migrations.AlterField(
            model_name='paymentstatus',
            name='title',
            field=models.CharField(default='', max_length=255, unique=True, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eshop.brand', verbose_name='برند'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.PositiveIntegerField(default=100, verbose_name='تعداد'),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='', null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='product',
            name='has_tax',
            field=models.BooleanField(default=False, verbose_name='مالیات اضافه شود'),
        ),
        migrations.AlterField(
            model_name='product',
            name='has_value_added_tax',
            field=models.BooleanField(default=False, verbose_name='افزودن مالیات بر ارزش افزوده'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=main_config.tools.UploadToPathAndRename('products'), verbose_name='تصویر محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='ویژه'),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_keywords',
            field=models.CharField(blank=True, help_text="separate with comma (used in the site's header for seo)", max_length=200, null=True, verbose_name='کلمات کلیدی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ ویرایش'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tax_percent',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='درصد مالیات'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=200, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='product',
            name='view',
            field=models.PositiveIntegerField(default=0, verbose_name='بازدید'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.PositiveIntegerField(default=0, help_text='input value as Grams', verbose_name='وزن'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to=main_config.tools.UploadToPathAndRename('products'), verbose_name='تصویر محصول'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.product', verbose_name='محصول'),
        ),
        migrations.AlterField(
            model_name='productmonetaryoption',
            name='option',
            field=models.CharField(max_length=200, verbose_name='آپشن'),
        ),
        migrations.AlterField(
            model_name='productmonetaryoption',
            name='price',
            field=models.PositiveIntegerField(default=0, help_text='Toman', verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='productmonetaryoption',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.product', verbose_name='محصول'),
        ),
        migrations.AlterField(
            model_name='productproperty',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='productproperty',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ ویرایش'),
        ),
        migrations.AlterField(
            model_name='productproperty',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.product', verbose_name='محصول'),
        ),
        migrations.AlterField(
            model_name='productproperty',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='productproperty',
            name='value',
            field=models.CharField(default='', max_length=255, verbose_name='مقدار'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='has_value_added_tax',
            field=models.BooleanField(default=True, verbose_name='افزودن مالیات بر ارزش افزوده'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ ویرایش'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='product_finishing_alert',
            field=models.PositiveIntegerField(default=10, verbose_name='حداقل تعداد هشدار اتمام محصول'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='site_icon',
            field=models.ImageField(upload_to=main_config.tools.UploadToPathAndRename('setting'), verbose_name='آیکون سایت (favicon)'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='site_logo',
            field=models.ImageField(upload_to=main_config.tools.UploadToPathAndRename('setting'), verbose_name='لوگوی سایت'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='site_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان سایت'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='soomasoft_webservice_otp_number',
            field=models.CharField(default='', max_length=50, verbose_name='کد otp سوماسافت'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='soomasoft_webservice_password',
            field=models.CharField(default='', max_length=50, verbose_name='رمز عبور وب سرویس سوماسافت'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='soomasoft_webservice_user',
            field=models.CharField(default='', max_length=50, verbose_name='نام کاربری وب سرویس سوماسافت'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='value_added_tax_percent',
            field=models.PositiveIntegerField(default=9, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='درصد مالیات بر ارزش افزوده'),
        ),
        migrations.AlterField(
            model_name='shippingcost',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='shippingcost',
            name='description',
            field=models.TextField(blank=True, default='', null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='shippingcost',
            name='from_weight',
            field=models.PositiveIntegerField(default=0, help_text='گرم', verbose_name='از وزن'),
        ),
        migrations.AlterField(
            model_name='shippingcost',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ ویرایش'),
        ),
        migrations.AlterField(
            model_name='shippingcost',
            name='price',
            field=models.PositiveIntegerField(default=0, help_text='toman', verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='shippingcost',
            name='states',
            field=models.ManyToManyField(to='admin_theme.State', verbose_name='استان های مقصد'),
        ),
        migrations.AlterField(
            model_name='shippingcost',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='shippingcost',
            name='to_weight',
            field=models.PositiveIntegerField(default=0, help_text='گرم', verbose_name='تا وزن'),
        ),
        migrations.AlterField(
            model_name='shippingmethod',
            name='code',
            field=models.PositiveSmallIntegerField(default=0, unique=True, verbose_name='کد'),
        ),
        migrations.AlterField(
            model_name='shippingmethod',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='shippingmethod',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ ویرایش'),
        ),
        migrations.AlterField(
            model_name='shippingmethod',
            name='payment_methods',
            field=models.ManyToManyField(to='eshop.PaymentMethod', verbose_name='روش های پرداخت'),
        ),
        migrations.AlterField(
            model_name='shippingmethod',
            name='title',
            field=models.CharField(max_length=200, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='shippingstatus',
            name='code',
            field=models.PositiveSmallIntegerField(default=0, unique=True, verbose_name='کد'),
        ),
        migrations.AlterField(
            model_name='shippingstatus',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='shippingstatus',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ ویرایش'),
        ),
        migrations.AlterField(
            model_name='shippingstatus',
            name='title',
            field=models.CharField(default='', max_length=255, unique=True, verbose_name='عنوان'),
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد')),
                ('modify_date', models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ ویرایش')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان آدرس')),
                ('receiver', models.CharField(max_length=100, verbose_name='نام و نام خانوادگی گیرنده')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='شماره تماس')),
                ('city', models.CharField(max_length=100, verbose_name='شهر')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('postcode', models.CharField(max_length=10, validators=[eshop.validators.validate_postcode], verbose_name='کد پستی')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_theme.state', verbose_name='استان')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'آدرس ارسال',
                'verbose_name_plural': 'آدرس های ارسال',
            },
        ),
    ]
