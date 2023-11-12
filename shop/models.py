from PIL import Image
from io import BytesIO

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext as _
from django.db.models.fields.files import ImageFieldFile
from django.core.files import File
from mptt.models import MPTTModel, TreeForeignKey
from main_config.tools import UploadToPathAndRename
from django.utils.safestring import mark_safe
from django.conf import settings
from ckeditor.fields import RichTextField


def get_image_field(self):
    output = []
    for k, v in self.__dict__.items():
        if isinstance(v, ImageFieldFile):
            output.append(k)
    return output


class MainModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name=_("create date"))
    modify_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name=_("modify date"))
    is_active = models.BooleanField(default=True, verbose_name=_("is active"))

    def save(self, *args, **kwargs):
        image_fields = get_image_field(self)
        if image_fields:
            for i in image_fields:
                if hasattr(self, i) and isinstance(getattr(self, i), ImageFieldFile):
                    image = Image.open(getattr(self, i).file)
                    image_io = BytesIO()
                    image_extension = getattr(self, i).name.rpartition(".")[-1].upper()
                    image_extension = "JPEG" if image_extension == "JPG" else image_extension
                    image.save(image_io, image_extension, quality=60)
                    new_image = File(image_io, name=getattr(self, i).name)
                    setattr(self, i, new_image)
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


# class Category(models.Model):
#     title = models.CharField(max_length=200, verbose_name=_("title"))
#     description = models.TextField(default="",  verbose_name=_("description"), blank=True, null=True)
#
#     def __unicode__(self):
#         return self.title
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = _("category")
#         verbose_name_plural = _("categories")


class Category(MPTTModel):
    title = models.CharField(max_length=200, verbose_name=_("title"))
    description = models.TextField(default="",  verbose_name=_("description"), blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")


class Brand(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("title"))
    description = models.TextField(default="",  verbose_name=_("description"), blank=True, null=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("brand")
        verbose_name_plural = _("brands")


class PaymentMethod(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("title"))
    code = models.PositiveSmallIntegerField(default=0, verbose_name=_("code"), unique=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("paymwent method")
        verbose_name_plural = _("payment methods")


class ShippingMethod(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("title"))
    code = models.PositiveSmallIntegerField(default=0, verbose_name=_("code"), unique=True)
    payment_methods = models.ManyToManyField(PaymentMethod, verbose_name=_("payment methods"))

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("shipping method")
        verbose_name_plural = _("shipping methods")


class Product(MainModel):
    title = models.CharField(max_length=200, verbose_name=_("title"))
    image = models.ImageField(verbose_name=_("product image"), upload_to=UploadToPathAndRename("products"))
    category = models.ForeignKey(Category, verbose_name=_("category"), on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, verbose_name=_("brand"), blank=True, null=True, on_delete=models.CASCADE)
    description = models.TextField(default="",  verbose_name=_("description"), blank=True, null=True)
    price = models.PositiveIntegerField(default=0, verbose_name=_("price"))
    view = models.PositiveIntegerField(default=0, verbose_name=_("view"))
    weight = models.PositiveIntegerField(default=0, verbose_name=_("weight"), help_text=_("input value as Grams"))
    count = models.PositiveIntegerField(default=100, verbose_name=_("count"))
    shipping_methods = models.ManyToManyField(ShippingMethod, verbose_name=_("shipping merthods"))
    is_featured = models.BooleanField(default=False, verbose_name=_("is featured"))
    min_purchase = models.PositiveIntegerField(default=0, verbose_name=_("minimum purchase"))
    max_purchase = models.PositiveIntegerField(default=100, verbose_name=_("maximum purchase"))
    has_value_added_tax = models.BooleanField(default=True, verbose_name=_("has value added tax"))

    def image_tag(self):
        return mark_safe(f'<img src="{settings.MEDIA_URL}{self.image}" height="50" />')
    image_tag.allow_tags = True
    image_tag.short_description = "---"

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
        unique_together = [["title", "category"], ["title", "brand"]]


class ProductImage(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE)
    image = models.ImageField(verbose_name=_("product image"), upload_to=UploadToPathAndRename("products"))

    def __unicode__(self):
        return self.product.title

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = _("product image")
        verbose_name_plural = _("product images")


class ProductOption(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE)
    option = models.CharField(max_length=200, verbose_name=_("option"))

    def __unicode__(self):
        return self.product.title

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = _("product option")
        verbose_name_plural = _("product options")


class ProductMonetaryOption(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE)
    option = models.CharField(max_length=200, verbose_name=_("option"))
    price = models.PositiveIntegerField(default=0, verbose_name=_("price"), help_text="Toman")

    def __unicode__(self):
        return self.product.title

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = _("product monetary option")
        verbose_name_plural = _("product monetary options")


class Discount(MainModel):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name=_("product"))
    percent = models.PositiveIntegerField(default=0, verbose_name=_("discount percent"), validators=[MaxValueValidator(100), MinValueValidator(1)])

    class Meta:
        verbose_name = _("discount")
        verbose_name_plural = _("discounts")

    def __unicode__(self):
        return f"{str(self.product)} - {str(self.percent)}"

    def __str__(self):
        return f"{str(self.product)} - {str(self.percent)}"


class Cart(MainModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("user"))

    class Meta:
        verbose_name = _("cart")
        verbose_name_plural = _("carts")

    def __unicode__(self):
        return str(self.user)

    def __str__(self):
        return str(self.user)


class CartItem(MainModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name=_("cart"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("product"))
    monetary_option = models.ForeignKey(ProductMonetaryOption, on_delete=models.CASCADE, verbose_name=_("monetary option"), null=True, blank=True)
    count = models.PositiveIntegerField(default=1, verbose_name=_("count"), validators=[MinValueValidator(1)])
    price = models.PositiveIntegerField(default=0, verbose_name=_("price"))

    class Meta:
        verbose_name = _("cart item")
        verbose_name_plural = _("cart items")

    def __unicode__(self):
        return f"{str(self.cart)} - {self.product} - {self.count}"

    def __str__(self):
        return f"{str(self.cart)} - {self.product} - {self.count}"


class Setting(MainModel):
    title = models.CharField(max_length=200, verbose_name=_("title"), blank=True, null=True)
    site_title = models.CharField(max_length=200, verbose_name=_("site title"), blank=True, null=True)
    site_icon = models.ImageField(verbose_name=_("site icon"), upload_to=UploadToPathAndRename("setting"))
    site_logo = models.ImageField(verbose_name=_("site logo"), upload_to=UploadToPathAndRename("setting"))
    contact_us = RichTextField()
    product_finishing_alert = models.PositiveIntegerField(default=10, verbose_name=_("product finishing alert"))
    value_added_tax_percent = models.PositiveIntegerField(default=9, verbose_name=_("value added tax percent"), validators=[MaxValueValidator(100), MinValueValidator(1)])

    class Meta:
        verbose_name = _("settings")
        verbose_name_plural = _("settings")

    def __unicode__(self):
        return str(self.title)

    def __str__(self):
        return str(self.title)
