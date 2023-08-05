from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Home Page URL
    path("", TemplateView.as_view(template_name="index.html")),

    # Profiles URLs
    path("", include("profiles.urls")),

    # Sighting URLs
    path("", include("sighting.urls")),

    # Posts URLs
    path("", include("posts.urls")),
]
