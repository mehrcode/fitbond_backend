from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer, UserModelSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated , AllowAny


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password1 = request.data.get("password1")
        password2 = request.data.get("password2")

        if password1 != password2:
            return Response({"error": "password does not match"}, status=400)

        data = {
            "email": email,
            "password": password1,
        }
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "user is created"}, status=201)

        return Response({"error": serializer.errors}, status=400)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone": user.phone,
            "date_joined": user.date_joined,
            "last_login": user.last_login,
        }
        serializer = UserModelSerializer(data=data)
        return Response(data)
    
class EditProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        data = {
            "phone": request.data.get("phone"),
            "first_name": request.data.get("first_name"),
            "last_name": request.data.get("last_name")
        }

        cleaned_data = {k: v for k, v in data.items() if v != ""}
        serializer = UserModelSerializer(user ,data=cleaned_data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profile is updated."}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)