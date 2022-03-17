# apps/evas/Test_evas/test_eva.py

from django.test import TestCase
from django.urls import reverse
from apps.evas.views import Eva


class EvaTests(TestCase):
    def setUp(self):
        self.astronaut = Eva.objects.create(
            # code="EVA9999",
            # mission="Test mission",
            astronaut="/astronauts/56b4d467-12bb-4136-aa1b-dcaf1c59a469",
            type="Test type",
            date="1964-03-10",
            duration_secse="00:00:01",
            tethered="Test tethered",
            planned="Test planned",
            notes="Test notes test notes test notes test notes",
        )

    def test_eva_listing(self):
        # self.assertEqual(f"{self.eva.code}", "EVA9999")
        # self.assertEqual(f"{self.eva.mission}", "")
        self.assertEqual(
            f"{self.eva.astronaut}", "/astronauts/56b4d467-12bb-4136-aa1b-dcaf1c59a469"
        )
        self.assertEqual(f"{self.eva.type}", "Test type")
        self.assertEqual(f"{self.eva.date}", "1964-03-10")
        self.assertEqual(f"{self.evat.duration_secs}", "00:00:01")
        self.assertEqual(f"{self.eva.tethered}", "Test tethered")
        self.assertEqual(f"{self.eva.planned}", "Test planned")
        self.assertEqual(
            f"{self.eva.notes}", "Test notes test notes test notes test notes"
        )

    def test_eva_list_view(self):
        response = self.client.get(reverse("eva_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, "/astronauts/56b4d467-12bb-4136-aa1b-dcaf1c59a469"
        )
        self.assertTemplateUsed(response, "evas/eva_list.html")

    def test_eva_detail(self):
        response = self.client.get(self.eva.get_absolute_url())
        no_response = self.client.get("/eva/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Test notes test notes test notes test notes")
        self.assertTemplateUsed(response, "evas/eva_detail.html")
