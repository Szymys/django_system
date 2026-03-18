from django.contrib import admin
from .models import StoreSettings




@admin.register(StoreSettings)
class StoreSettingsAdmin(admin.ModelAdmin):
    list_display = ("store_name", "navbar_color")
    fields = ("store_name", "store_description", "navbar_color")



    def has_add_permission(self, request):

        # pozwala dodac tylko jeden rekord
        if StoreSettings.objects.exists():
            return False
        return super().has_add_permission(request)


# opcjonalnie blokujemy usuwanie
    def has_delete_permission(self, request, obj=None):
        
        return False