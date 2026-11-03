from django.db import models
from django.conf import settings

# Create your models here.
class Document(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="documents",
    )
    title = models.CharField(max_length=255)
    content = models.TextField()

    file = models.FileField(
        upload_to="documents/",
        null=True,
        blank=True
    )

    original_filename = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    file_size = models.PositiveBigIntegerField(null=True, blank=True)
    file_type = models.CharField(max_length=50, null=True, blank=True)
    uploaded_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title