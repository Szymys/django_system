from .models import StoreSettings

# funkcja dostaje request i zwraca tekst do szablonow
def store_settings(request):
    settings = StoreSettings.objects.first()

    return {
        "global_store_name": settings.store_name if settings else "Mój sklep",
        "global_store_description": settings.store_description if settings else "",
    }