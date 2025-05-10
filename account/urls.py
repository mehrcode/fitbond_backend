from django.urls import path
from . import views
from django.http import HttpResponse


urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
]
