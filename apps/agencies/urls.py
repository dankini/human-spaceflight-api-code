# apps/agencies/urls.py

from django.urls import path
from apps.agencies.views import AgencyListView, AgencyDetailView

urlpatterns = [
    path("", AgencyListView.as_view(), name="agency_list"),
    path("<uuid:pk>", AgencyDetailView.as_view(), name="agency_detail"),
]
