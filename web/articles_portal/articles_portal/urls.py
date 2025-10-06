from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('article/', include('app.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]
