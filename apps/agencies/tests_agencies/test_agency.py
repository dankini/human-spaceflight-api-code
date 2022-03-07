# apps/agencies/Tes_agencies/test_agency.py

from django.test import TestCase
from django.urls import reverse
from apps.agencies.views import Agency


class AgencyTests(TestCase):
    def setUp(self):
        self.agency = Agency.objects.create(
            name="Test space agency",
            abbreviation="TSS",
            country="Republic of Test",
            formed_date="2022-03-04",
            website="www.testagency.com",
        )

    def test_agency_listing(self):
        self.assertEqual(f"{self.agency.name}", "Test space agency")
        self.assertEqual(f"{self.agency.abbreviation}", "TSS")
        self.assertEqual(f"{self.agency.country}", "Republic of Test")
        self.assertEqual(f"{self.agency.formed_date}", "2022-03-04")
        self.assertEqual(f"{self.agency.website}", "www.testagency.com")

    def test_agency_list_view(self):
        response = self.client.get(reverse("agency_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test space agency")
        self.assertTemplateUsed(response, "agencies/agency_list.html")

    def test_agency_detail(self):
        response = self.client.get(self.agency.get_absolute_url())
        no_response = self.client.get("/agency/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Test space agency")
        self.assertTemplateUsed(response, "agencies/agency_detail.html")
