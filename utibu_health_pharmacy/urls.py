from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from utibu_health_pharmacy import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index),
    path('pharmacy/', include('pharmacy.urls'))
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # In production, static files should be served by Whitenoise or a dedicated web server
    # Media files should be served by the web server directly
    pass
