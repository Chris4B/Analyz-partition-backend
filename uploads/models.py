from django.db import models

# Create your models here.
class UploadedFile(models.Model):
    """
    Model to store uploaded files.

    Attributes:
        file (FileField): The uploaded file, stored in the 'uploads/' directory.
        uploaded_at (DateTimeField): Timestamp indicating when the file was uploaded.
    """
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name