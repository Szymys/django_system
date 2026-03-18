from django.db import models


class StoreSettings(models.Model):
    NAVBAR_COLOR_CHOICES = [
        ("orange", "Orange"),
        ("yellow", "Yellow"),
        ("green", "Green"),
        ("blue", "Blue"),
    ]



    store_name = models.CharField(max_length=100, verbose_name="Name")
    store_description = models.TextField(blank=True, verbose_name="Description")
    navbar_color = models.CharField(
        max_length=20,
        choices=NAVBAR_COLOR_CHOICES,
        default="orange",
        verbose_name="Navbar color",
    )




    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"

    def __str__(self):
        return self.store_name

    def get_navbar_color_hex(self):
        colors = {
            "orange": "#CE4A02",
            "yellow": "#C99700",
            "green": "#198754",
            "blue": "#0D6EFD",
        }
        return colors.get(self.navbar_color, "#CE4A02")