from rest_framework import serializers
from .models import ImageHash

class ImageHashSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageHash
        fields = '__all__'