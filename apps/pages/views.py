# apps/pages/views.py

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """Class docstring."""

    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    """Class docstring."""

    template_name = "pages/about.html"
