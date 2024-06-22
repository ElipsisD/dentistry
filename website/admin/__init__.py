from .contacts import ContactsAdmin
from .discount import DiscountAdmin
from .notification import NotificationAdmin
from .price import PriceFileAdmin, PriceSectionAdmin
from .service import ServiceAdmin
from .specialist import SpecialistAdmin

__all__ = [
    "ContactsAdmin",
    "SpecialistAdmin",
    "NotificationAdmin",
    "PriceSectionAdmin",
    "PriceFileAdmin",
    "DiscountAdmin",
    "ServiceAdmin",
]
