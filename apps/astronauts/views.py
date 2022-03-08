# apps/astronauts/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from apps.astronauts.models import Astronaut


class AstronautListView(ListView):
    model = Astronaut
    context_object_name = "astronaut_list"
    template_name = "astronauts/astronaut_list.html"


class AstronautDetailView(DetailView):
    model = Astronaut
    context_object_name = "astronaut"
    template_name = "astronauts/astronaut_detail.html"
