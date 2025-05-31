from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.models import User, Group
from .models import Habit, Log
from .serializers import HabitSerializer, GroupSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


from rest_framework.permissions import IsAuthenticated


class HabitCreateView(APIView):
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        user = request.user
        data = request.data
        habit = Habit.objects.create(
            user=user,
            walking_steps=data.get("walking_steps", 0),
            exercise_minutes=data.get("exercise_minutes", 0),
            exercise_description=data.get("exercise_description", ""),
        )
        return Response({"message": "Habit log created"}, status=201)


class GroupView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        name = request.data.get("name")
        member_ids = request.data.get("member_ids", [])

        if not name:
            return Response({"error": "Group name is required."}, status=400)

        admin = request.user  # Ensure request.user is authenticated
        group = Group.objects.create(
            name=name, admin=admin
        )  # ✅ Matches the model definition
        group.members.add(admin)

        for member_id in member_ids:
            try:
                user = User.objects.get(id=member_id)
                group.members.add(user)
            except User.DoesNotExist:
                continue

        serializer = GroupSerializer(group)
        return Response(serializer.data, status=201)


class SubmitCountView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        habits = Habit.objects.filter(user=user)

        submit_times = habits.count()
        active_days = habits.values_list("created_at", flat=True).distinct().count()

        return Response({"submit_count": submit_times, "active_days": active_days})
