from django.db import models
from django.utils.text import slugify

class Trip(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(max_length=1500)
    slug = models.SlugField(max_length=255, unique=True, blank=True)  # Поле slug

    class Meta:
        verbose_name = "Trip"
        verbose_name_plural = "Trips"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Генерация slug на основе name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

