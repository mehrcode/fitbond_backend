from django.urls import path
from .views import (
    HabitCreateView, SubmitCountView, StreakView

)

urlpatterns = [
    path('logs-create/', HabitCreateView.as_view(), name='log-create'),
    path('submit-count/', SubmitCountView.as_view(), name='submit-count'),
    path('streak/', StreakView.as_view(), name='habit-streak'),
]