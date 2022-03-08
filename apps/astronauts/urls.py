# apps/astronauts/urls.py

from django.urls import path
from apps.astronauts.views import AstronautListView, AstronautDetailView

urlpatterns = [
    path("", AstronautListView.as_view(), name="astronaut_list"),
    path("<uuid:pk>", AstronautDetailView.as_view(), name="astronaut_detail"),
]
