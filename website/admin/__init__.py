from .application import ApplicationAdmin
from .contacts import ContactsAdmin
from .discount import DiscountAdmin
from .feedback import FeedbackAdmin
from .notification import NotificationAdmin
from .price import PriceFileAdmin, PriceSectionAdmin
from .service import ServiceAdmin
from .specialist import SpecialistAdmin

__all__ = [
    "ApplicationAdmin",
    "ContactsAdmin",
    "SpecialistAdmin",
    "NotificationAdmin",
    "PriceSectionAdmin",
    "PriceFileAdmin",
    "DiscountAdmin",
    "ServiceAdmin",
    "FeedbackAdmin",
]
