from django.urls import include, path
from rest_framework import routers

from website.api.handlers.application import ApplicationAPI
from website.api.handlers.contacts import ContactsAPI
from website.api.handlers.discount import DiscountAPI
from website.api.handlers.feedback import FeedbackAPI
from website.api.handlers.file import FileAPI
from website.api.handlers.notification import NotificationAPI
from website.api.handlers.price import PriceAPI
from website.api.handlers.service import ServiceAPI, ServiceCarouselAPI
from website.api.handlers.specialist import CarouselSpecialistAPI, SpecialistAPI

router = routers.DefaultRouter()

router.register("specialists", SpecialistAPI, basename="specialists")
router.register("carousel-specialists", CarouselSpecialistAPI, basename="carousel_specialists")
router.register("contacts", ContactsAPI, basename="contacts")
router.register("notification", NotificationAPI, basename="notification")
router.register("feedback", FeedbackAPI, basename="feedback")
router.register("application", ApplicationAPI, basename="application")
router.register("price", PriceAPI, basename="price")
router.register("file", FileAPI, basename="file")
router.register("discount", DiscountAPI, basename="discount")
router.register("service", ServiceAPI, basename="service")
router.register("carousel-service", ServiceCarouselAPI, basename="carousel_service")

urlpatterns = [
    path("", include(router.urls)),
]
