from .models import StoreSettings

# funkcja dostaje request i zwraca tekst do szablonow
def store_settings(request):
    settings = StoreSettings.objects.first()

    return {
        "global_store_name": settings.store_name if settings else "Mój sklep",
        "global_store_description": settings.store_description if settings else "",
        "global_navbar_color": settings.get_navbar_color_hex() if settings else "#CE4A02",
    }