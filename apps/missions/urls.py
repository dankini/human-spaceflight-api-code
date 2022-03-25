# apps/missions/urls.py

from django.urls import path
from apps.missions.views import MissionListView, MissionDetailView

urlpatterns = [
    path("", MissionListView.as_view(), name="mission_list"),
    path("<uuid:pk>", MissionDetailView.as_view(), name="mission_detail"),
    # path("crew/<uuid:pk>", CrewListView.as_view(), name="crew_list"),
    # path("crew-member/<uuid:pk>", CrewDetailView.as_view(), name="crew_detail"),
]
