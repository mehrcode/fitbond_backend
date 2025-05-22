from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# Define the home view function
def home(request):
    return HttpResponse("صفحه‌ی اصلی کار می‌کند!")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("account.urls")),
    path("habit/", include("habit.urls")),
    path("api/account/", include("account.api.urls")),
    path("api/account/register", include("account.api.urls")),

    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", home, name="home"),
]
