from django.db import models




class StoreSettings(models.Model):
    store_name = models.CharField(max_length=100, verbose_name="Name")
    store_description = models.TextField(blank=True, verbose_name="Description")

    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"

    def __str__(self):
        return self.store_name