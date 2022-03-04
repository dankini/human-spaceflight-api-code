# apps/agencies/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from apps.agencies.models import Agency


class AgencyListView(ListView):
    model = Agency
    context_object_name = "agency_list"
    template_name = "agencies/agency_list.html"


class AgencyDetailView(DetailView):
    model = Agency
    context_object_name = "agency"
    template_name = "agencies/agency_detail.html"
