from django.urls import path
from .views import (
    LogCreateView, GroupView, SubmitCountView, StreakView

)

urlpatterns = [
    path('logs/create/', LogCreateView.as_view(), name='log-create'),
    path('groups/create/', GroupView.as_view(), name='group-create'),
    path('submit-count/', SubmitCountView.as_view(), name='submit-count'),
    path('streak/', StreakView.as_view(), name='habit-streak'),
]