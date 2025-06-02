from rest_framework import serializers
from .models import Habit, Group, User


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


class GroupSerializer(serializers.ModelSerializer):
    admin = serializers.StringRelatedField()
    members = serializers.StringRelatedField(many=True)

    class Meta:
        model = Group
        fields = ["id", "name", "admin", "members", "created_at"]
        read_only_fields = ["admin", "created_at"]
