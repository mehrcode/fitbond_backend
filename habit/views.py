from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import User
from .models import Habit
from .serializers import HabitSerializer
from rest_framework.permissions import IsAuthenticated
from datetime import date, timedelta


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
        return Response({"message": "Habit created"}, status=201)


class SubmitCountView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        habits = Habit.objects.filter(user=user)

        submit_times = habits.count()
        active_days = habits.values_list("created_at", flat=True).distinct().count()

        return Response({"submit_count": submit_times, "active_days": active_days})


class StreakView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        habits = Habit.objects.filter(user=user).values_list("created_at", flat=True)
        habit_dates = set(habits)

        today = date.today()
        streak = 0
        current_day = today

        while current_day in habit_dates:
            streak += 1
            current_day -= timedelta(days=1)

        return Response({"streak": streak})
