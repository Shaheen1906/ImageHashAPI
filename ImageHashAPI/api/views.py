import requests
import hashlib
from PIL import Image
import imagehash as ihash
from io import BytesIO
from rest_framework import generics , serializers
from .models import ImageHash
from .serializers import ImageHashSerializer

class ImageHashCreateAPIView(generics.CreateAPIView):
    queryset = ImageHash.objects.all()
    serializer_class = ImageHashSerializer

    def perform_create(self, serializer):
        image_url = self.request.data.get('image_url')
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content))

            # Calculate MD5
            md5_hash = hashlib.md5(response.content).hexdigest()

            # Calculate pHash
            phash = str(ihash.phash(image))

            serializer.save(md5_hash=md5_hash, phash=phash)
        except requests.RequestException:
            raise serializers.ValidationError("Invalid image URL or unable to fetch the image.")
        except Exception as e:
            raise serializers.ValidationError(f"Error processing image: {str(e)}")

class ImageHashListAPIView(generics.ListAPIView):
    queryset = ImageHash.objects.all()
    serializer_class = ImageHashSerializer

class ImageHashDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageHash.objects.all()
    serializer_class = ImageHashSerializer
