from django.db import models

class ImageHash(models.Model):
    image_url = models.URLField(unique=True)
    md5_hash = models.CharField(max_length=32, editable=False)
    phash = models.CharField(max_length=64, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_url
    


