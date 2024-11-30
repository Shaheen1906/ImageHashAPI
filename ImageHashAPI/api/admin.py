from django.contrib import admin
from .models import ImageHash


class ImagehashAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_url', 'md5_hash', 'phash']

admin.site.register(ImageHash, ImagehashAdmin)