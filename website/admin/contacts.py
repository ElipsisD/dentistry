from django.contrib import admin
from solo.admin import SingletonModelAdmin

from website.models import Contacts


@admin.register(Contacts)
class ContactsAdmin(SingletonModelAdmin):
    ...
