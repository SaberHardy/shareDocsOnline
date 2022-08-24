from django.db import models


class Document(models.Model):
    description = models.TextField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.document.name)

    # def doc_size(self):
    #     return int(self.document.size) / 1024
