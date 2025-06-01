from django.db import models
from account.models import User

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    walking_steps = models.IntegerField(default=0)
    exercise_minutes = models.IntegerField(default=0)
    exercise_description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def date(self):
        return self.created_at

    def __str__(self):
        return f"{self.user.username} - {self.date()}"


class Group(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="admin_groups"
    )
    members = models.ManyToManyField(User, related_name="habit_groups")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
