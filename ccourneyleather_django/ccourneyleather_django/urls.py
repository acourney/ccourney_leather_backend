from django.conf.urls import include
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('users.urls')),
    path('', include('ccourneyleather.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
