from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('products/', include('eshop_products.urls')),
    path('accounts/', include('eshop_accounts.urls')),
    path('contact/', include('eshop_contact.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
