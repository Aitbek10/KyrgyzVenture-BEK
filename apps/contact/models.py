from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f"Message from {self.name}"