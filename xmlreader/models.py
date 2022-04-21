from django.db import models


class Upload(models.Model):
    file = models.FileField(upload_to="xml_files")
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file}"
