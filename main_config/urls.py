from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from eshop.views import home, product


urlpatterns = [
    path('', home, name="homepage"),
    path('product/<int:product_id>/', product, name="product"),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
