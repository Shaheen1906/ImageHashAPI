from django.urls import path
from .views import ImageHashCreateAPIView, ImageHashListAPIView, ImageHashDetailAPIView

urlpatterns = [
    path('create/', ImageHashCreateAPIView.as_view(), name='imagehash-create'),
    path('list/', ImageHashListAPIView.as_view(), name='imagehash-list'),
    path('list/<int:pk>/', ImageHashDetailAPIView.as_view(), name='imagehash-detail'),
]
