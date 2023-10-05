from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from shop.views import time, home

urlpatterns = [
    path('', home, name="homepage"),
    path('time/', time),
    path('time/plus/<int:hour>/', time),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
