from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # Указываем, что поля могут быть пустыми и разрешены null-значения
    image1 = models.ImageField(upload_to='images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name = "Destination"
        verbose_name_plural = "Destinations"

    def __str__(self):
        return self.name
