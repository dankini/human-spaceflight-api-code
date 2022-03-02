# apps/pages/test_homepage.py

from django.test import SimpleTestCase
from django.urls import reverse, resolve

from apps.pages.views import HomePageView


class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "pages/home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(
            self.response,
            "From the first solo mission into space to the last crewed lunar landing",
        )

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "I should not be on this page")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
