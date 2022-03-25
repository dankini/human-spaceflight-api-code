# apps/missions/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from apps.missions.models import Mission


class MissionListView(ListView):
    model = Mission
    context_object_name = "mission_list"
    template_name = "missions/mission_list.html"


class MissionDetailView(DetailView):
    model = Mission
    context_object_name = "mission"
    template_name = "missions/mission_detail.html"


"""
class CrewListView(ListView):
    model = Mission
    context_object_name = "crew_list"
    template_name = "missions/mission_list.html"


class CrewDetailView(DetailView):
    model = Mission
    context_object_name = "mission"
    template_name = "missions/crew_detail.html"
"""
