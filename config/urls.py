from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from core.utils.healthcheck import healthcheck

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/health/", healthcheck, name="healthcheck"),
    path("api/website/", include("website.api.urls")),
    path("_nested_admin/", include("nested_admin.urls")),
]

if settings.DEBUG:
    from django.views.decorators.cache import never_cache
    from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

    urlpatterns += [
        path("api/schema/", never_cache(SpectacularAPIView.as_view()), name="schema"),
        path("api/swagger/", never_cache(SpectacularSwaggerView.as_view(url_name="schema")), name="swagger"),
        path("api/redoc/", never_cache(SpectacularRedocView.as_view(url_name="schema")), name="redoc"),
    ]

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
