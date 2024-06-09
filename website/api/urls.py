from django.urls import include, path
from rest_framework import routers

from website.api.handlers.contacts import ContactsAPI
from website.api.handlers.notification import NotificationAPI
from website.api.handlers.price import PriceAPI
from website.api.handlers.specialist import SpecialistAPI

router = routers.DefaultRouter()

router.register("specialists", SpecialistAPI, basename="specialists")
router.register("contacts", ContactsAPI, basename="contacts")
router.register("notification", NotificationAPI, basename="notification")
router.register("price", PriceAPI, basename="price")

urlpatterns = [
    path("", include(router.urls)),
]
