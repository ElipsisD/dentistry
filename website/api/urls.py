from django.conf import settings
from django.urls import include, path
from rest_framework import routers

from website.api.handlers.contacts import ContactsAPI
from website.api.handlers.specialist import SpecialistAPI

router = routers.DefaultRouter()

router.register("specialists", SpecialistAPI, basename="specialists")
router.register("contacts", ContactsAPI, basename="contacts")

urlpatterns = [
    path("", include(router.urls)),
]

if settings.DEBUG:
    from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

    urlpatterns += [
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
        path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
        path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    ]
