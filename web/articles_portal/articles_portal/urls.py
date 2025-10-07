from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(pattern_name="home")),
    path("article/", include('app.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path("accounts/", include("allauth.urls")),
]
