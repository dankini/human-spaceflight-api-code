# apps/evas/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from apps.evas.models import Eva


class EvaListView(ListView):
    model = Eva
    context_object_name = "eva_list"
    template_name = "evas/eva_list.html"


class EvaDetailView(DetailView):
    model = Eva
    context_object_name = "eva"
    template_name = "evas/eva_detail.html"
