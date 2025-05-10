from django.urls import path
from .views import (
    HabitCreateView,

)

urlpatterns = [
    path('logs/create/', HabitCreateView.as_view(), name='habit-create'),
]