from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('gamestromadmin/', admin.site.urls),
    path('guardian/', include('guardian.urls')),
    path('', include('core.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
