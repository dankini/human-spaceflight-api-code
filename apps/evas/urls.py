# apps/evas/urls.py

from django.urls import path
from apps.evas.views import EvaListView, EvaDetailView

urlpatterns = [
    path("", EvaListView.as_view(), name="eva_list"),
    path("<uuid:pk>", EvaDetailView.as_view(), name="eva_detail"),
]
