from django.contrib import admin
from .models import Habit, Group


class HabitAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "date",
        "walking_steps",
        "exercise_minutes",
        "exercise_description",
    ]


admin.site.register(Habit, HabitAdmin)
admin.site.register(Group)
