from rest_framework import serializers
from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['user_id', 'walking_steps', 'exercise_minutes', 'exercise_description']