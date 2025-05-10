from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.models import User
from .models import Habit
from .serializers import HabitSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404


class HabitCreateView(APIView):
    permission_classes = []

    def post(self, request):
        user_id = request.data.get("user_id")
        if not user_id:
            return Response({"error": "User ID is required"}, status=400)

        user = get_object_or_404(User, id=user_id)  # Get user manually
        
        habit = Habit.objects.create(
            user=user,
            walking_steps=request.data.get("walking_steps"),
            exercise_minutes=request.data.get("exercise_minutes"),
            exercise_description=request.data.get("exercise_description"),
        )
        habit.save()

        return Response({"message": "Habit log created"}, status=201)
