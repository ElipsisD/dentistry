from django.contrib import admin

from website.models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    ...
