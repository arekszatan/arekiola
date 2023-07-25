from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('shopping.urls')),
    path('', include('wallet.urls')),
    path('', include('settings.urls')),
    path('', include('shoppingOther.urls')),
    path('', include('dreams.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
