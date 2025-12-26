from rest_framework import generics, permissions
from .models import Publication
from .serializers import PublicationSerializer
from django.contrib.auth.models import User
from rest_framework.exceptions import NotFound

# Create publication
class CreatePublicationAPI(generics.CreateAPIView):
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user=self.request.user)

# Get all publications of logged-in user

class UserPublicationsByIdAPI(generics.ListAPIView):
    serializer_class = PublicationSerializer
    permission_classes = [permissions.AllowAny]  # anyone can view

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound("User not found")
        return Publication.objects.filter(user=user)

# Update publication
class UpdatePublicationAPI(generics.UpdateAPIView):
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Publication.objects.filter(user=self.request.user)

# Delete publication
class DeletePublicationAPI(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Publication.objects.filter(user=self.request.user)

