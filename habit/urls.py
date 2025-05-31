from django.urls import path
from .views import (
    HabitCreateView, GroupView, SubmitCountView

)

urlpatterns = [
    path('logs/create/', HabitCreateView.as_view(), name='habit-create'),
    path('groups/create/', GroupView.as_view(), name='group-create'),
    path('submit-count/', SubmitCountView.as_view(), name='submit-count')
]