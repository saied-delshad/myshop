from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from shop.models import Category, Brand, PaymentMethod, ShippingMethod, Product, ProductImage, ProductOption, \
    ProductMonetaryOption, Setting, Discount, Cart, CartItem


# from shop.models import Publisher


# @admin.register(Publisher)
# class PublisherAdmin(admin.ModelAdmin):
#     def get_fields(self, request, obj=None):
#         return ["name", "address", "city", "country", "website"]
#
#     def get_list_display(self, request):
#         return ["name", "address", "website"]
#
#     def get_search_fields(self, request):
#         return ["name", "address", "website"]
#
#     def get_list_filter(self, request, filters=None):
#         return ["city", "country"]

@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    def get_fields(self, request, obj=None):
        return ["title", "description", "parent"]

    def get_list_display(self, request):
        return ["title"]

    def get_search_fields(self, request):
        return ["title", "description"]

    # def get_list_filter(self, request, filters=None):
    #     return ["city", "country"]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        return ["title", "description"]

    def get_list_display(self, request):
        return ["title"]

    def get_search_fields(self, request):
        return ["title", "description"]


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        return ["product", "percent", "is_active"]

    def get_list_display(self, request):
        return ["product", "percent", "is_active"]

    def get_search_fields(self, request):
        return ["product__title", "percent"]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        return ["user", "is_active"]

    def get_list_display(self, request):
        return ["user", "is_active"]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        return ["cart", "product", "monetary_option", "count", "price", "is_active"]

    def get_list_display(self, request):
        return ["cart", "product", "monetary_option", "count", "price", "is_active"]


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        return ["title", "code"]

    def get_list_display(self, request):
        return ["title", "code"]

    def get_search_fields(self, request):
        return ["title", "code"]


@admin.register(ShippingMethod)
class ShippingMethodAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        return ["title", "code", "payment_methods"]

    def get_list_display(self, request):
        return ["title", "code"]

    def get_search_fields(self, request):
        return ["title", "code"]


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ["image"]
    extra = 1


class ProductOptionInline(admin.TabularInline):
    model = ProductOption
    fields = ["option"]
    extra = 1


class ProductMonetaryOptionInline(admin.TabularInline):
    model = ProductMonetaryOption
    fields = ["option", "price"]
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductOptionInline, ProductMonetaryOptionInline]

    def get_fields(self, request, obj=None):
        return ["title", "category", "brand", "image", "description", "price", "view", "weight", "count", "shipping_methods", "is_featured", "min_purchase", "max_purchase", "has_value_added_tax", "is_active"]

    def get_list_display(self, request):
        return ["title", "image_tag", "category", "brand", "price", "view", "count", "is_active"]

    def get_search_fields(self, request):
        return ["title", "category", "brand", "description", "price", "view", "weight", "count", "min_purchase", "max_purchase",]

    def get_list_filter(self, request, filters=None):
        return ["category", "brand", "is_featured", "has_value_added_tax", "is_active"]


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):

    def get_fields(self, request, obj=None):
        return ["title", "site_title", "site_icon", "site_logo", "contact_us", "product_finishing_alert", "value_added_tax_percent"]

    def get_list_display(self, request):
        return ["title"]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
