from django.urls import path
from .views import (
    HabitCreateView, GroupView

)

urlpatterns = [
    path('logs/create/', HabitCreateView.as_view(), name='habit-create'),
    path('groups/create/', GroupView.as_view(), name='group-create'),
]