from django.contrib import admin

from .models import Sample


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ("uuid", "name", "created_at")
    search_fields = ("name",)
    list_filter = ("created_at",)
    readonly_fields = ("uuid", "created_at", "updated_at")
