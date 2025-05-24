from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


# Define the home view function
def home(request):
    return HttpResponse("صفحه‌ی اصلی کار می‌کند!")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("account.urls")),
    path("habit/", include("habit.urls")),
    path("api/account/", include("account.api.urls")),
    path("", home, name="home"),
]
