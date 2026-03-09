from django.contrib import admin
from .models import StoreSettings




@admin.register(StoreSettings)
class StoreSettingsAdmin(admin.ModelAdmin):
    list_display = ("store_name",)
    fields = ("store_name", "store_description")

    def has_add_permission(self, request):
        # pozwala dodac tylko jeden rekord
        if StoreSettings.objects.exists():
            return False
        return super().has_add_permission(request)



    def has_delete_permission(self, request, obj=None):
        # opcjonalnie blokujemy usuwanie
        return False