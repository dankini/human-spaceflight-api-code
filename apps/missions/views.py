# apps/missions/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from apps.missions.models import Mission, Crew


class MissionListView(ListView):
    model = Mission
    context_object_name = "mission_list"
    template_name = "missions/mission_list.html"


class MissionDetailView(DetailView):
    model = Mission
    context_object_name = "mission"
    template_name = "missions/mission_detail.html"


class CrewListView(ListView):
    # queryset = Mission.objects.get(name="Apollo 11")
    model = Crew
    context_object_name = "crew_list"
    template_name = "missions/crew_list.html"


"""class MissionCrewListView(ListView):
    def get_mission_crew(request, selected_mission_name):
        selected_mission = Mission.objects.get(name=selected_mission_name)
        crew = selected_mission.crew_members.all()
        return crew
        """

class CrewDetailView(DetailView):
    model = Crew
    template_name = "missions/crew_detail.html"  # Ensure this template exists
