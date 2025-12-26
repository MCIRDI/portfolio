from django.urls import path
from .views import (
    CreatePublicationAPI,
    UpdatePublicationAPI,
    UserPublicationsByIdAPI,
    DeletePublicationAPI
)

urlpatterns = [
    path('create/', CreatePublicationAPI.as_view()),
  path('user/<int:user_id>/', UserPublicationsByIdAPI.as_view(), name='user-publications-by-id'),    path('update/<int:pk>/', UpdatePublicationAPI.as_view()),
    path('delete/<int:pk>/', DeletePublicationAPI.as_view()),
]
