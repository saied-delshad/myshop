from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from eshop.views import home, product, brand, category, search, add_cart_item, plus_cart_item, minus_cart_item, \
    del_cart_item, shipp_payment, shipping_address, create_factor, cart, print_factor, factor


urlpatterns = [
    path('', home, name="homepage"),
    path('product/<int:product_id>/', product, name="product"),
    path('addcartitem/', add_cart_item, name="add_cart_item"),
    path('pluscartitem/<int:cart_item_id>/', plus_cart_item, name="cart_item_plus"),
    path('minuscartitem/<int:cart_item_id>/', minus_cart_item, name="cart_item_minus"),
    path('delcartitem/<int:cart_item_id>/', del_cart_item, name="delete_cart_item"),
    path('shipping-address/', shipping_address, name="shipping_address"),
    path('shipp-payment/', shipp_payment, name="shipp_payment"),
    path('cart/', cart, name="cart"),
    path('factor/<str:uuid>', factor, name="factor"),
    path('create-factor/', create_factor, name="create_factor"),
    path('brand/<str:slug>/', brand, name="brand"),
    path('category/<str:slug>/', category, name="category"),
    path('search/<str:slug>/', search, name="search"),
    path('print-factor/<str:factor_id>/', print_factor, name="print_factor"),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
