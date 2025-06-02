from rest_framework import serializers
from .models import Habit, User


class HabitSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Habit
        fields = [
            "user",
            "walking_steps",
            "exercise_minutes",
            "exercise_description",
        ]



