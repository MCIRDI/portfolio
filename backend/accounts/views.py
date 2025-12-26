from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView  # for custom login view
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import UserSerializer

class RegisterAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # create token
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "user": serializer.data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)



class LoginAPI(APIView):
    permission_classes = [permissions.AllowAny]  # public endpoint

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=user.username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)