from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/users/', include('apps.users.api.urls')),
    path('api/web3auth/', include('apps.web3auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
