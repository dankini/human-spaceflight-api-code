# apps/missions/urls.py

from django.urls import path
from apps.missions.views import (
    MissionListView,
    MissionDetailView,
    CrewListView,
    CrewDetailView,
)

urlpatterns = [
    path("", MissionListView.as_view(), name="mission_list"),
    path("<uuid:pk>", MissionDetailView.as_view(), name="mission_detail"),
    path("crew/", CrewListView.as_view(), name="crew_list"),
    path("crew/<uuid:pk>", CrewDetailView.as_view(), name="crew_detail"),
]
