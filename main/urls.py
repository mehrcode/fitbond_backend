from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("account.urls")),
    path('habit/', include('habit.urls')),
    path('api/account/', include('account.api.urls')),
]
