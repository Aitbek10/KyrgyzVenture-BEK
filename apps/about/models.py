from django.db import models

class About(models.Model):
    history = models.TextField()
    mission = models.TextField(default="Стандартная миссия")
    vision = models.TextField(default="Стандартное видение")

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"

    def __str__(self):
        return self.history[:50]
