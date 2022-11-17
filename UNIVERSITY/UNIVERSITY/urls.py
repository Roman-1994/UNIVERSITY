
from django.contrib import admin
from django.urls import path, include, re_path

from univer.urls import router
from univer.drf_yasg import urlpatterns as drf_yasg


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('univer.urls')),
    path('', include(router.urls)),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

urlpatterns += drf_yasg
