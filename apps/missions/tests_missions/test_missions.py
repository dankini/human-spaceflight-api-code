# apps/missions/tests_missions/test_mission.py

from django.test import TestCase
from django.urls import reverse
from apps.evas.views import Eva
from apps.astronauts.views import Astronaut


class EvaTests(TestCase):
    # https://docs.djangoproject.com/en/4.0/topics/testing/tools/#django.test.TestCase.setUpTestData
    @classmethod
    def setUpTestData(cls):
        # First create astronaut based on test_astronauts.py format
        # Note only mandatory fields used, the rest commented out here
        cls.astronaut = Astronaut.objects.create(
            first_name="Test astronaut firstname",
            # middle_name="Test astronaut middlename",
            # nick_name="Test astronaut nickname",
            last_name="Test astronaut lastname",
            birth_date="1930-03-07",
            # birth_town_city="Test town",
            # birth_state="Test state",
            # birth_country="Test country",
            # death_date="2022-03-07",
            # resting_place="Test resting place",
            rank_attained="Test rank attained",
            service_branch="Test service branch",
            nationality="Test nationality",
            first_time_in_space_date="1965-03-07",
            total_duration_space_secs="00:00:01",
            # retirement_date="1972-03-07",
            # wikipedia_bio_website="www.testastronaut.com",
        )

        # Now create test EVA object. note astronaut line 'astronaut=cls.astronaut'
        cls.eva = Eva.objects.create(
            code="9999",
            # mission="Test mission",
            astronaut=cls.astronaut,
            type="SU",
            date="1964-03-10",
            duration_secs="00:00:01",
            tethered="TE",
            planned="PL",
            notes="Test notes test notes test notes test notes",
        )

    def test_eva_content(self):
        self.assertEqual(f"{self.eva.code}", "9999")
        # self.assertEqual(f"{self.eva.mission}", "")
        self.assertEqual(f"{self.eva.astronaut}", "Test astronaut lastname")
        self.assertEqual(f"{self.eva.type}", "SU")
        self.assertEqual(f"{self.eva.date}", "1964-03-10")
        self.assertEqual(f"{self.eva.duration_secs}", "00:00:01")
        self.assertEqual(f"{self.eva.tethered}", "TE")
        self.assertEqual(f"{self.eva.planned}", "PL")
        self.assertEqual(
            f"{self.eva.notes}", "Test notes test notes test notes test notes"
        )

    def test_eva_list_view(self):
        response = self.client.get(reverse("eva_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "est astronaut lastname")
        self.assertTemplateUsed(response, "evas/eva_list.html")

    def test_eva_detail(self):
        response = self.client.get(self.eva.get_absolute_url())
        no_response = self.client.get("/eva/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Test notes test notes test notes test notes")
        self.assertTemplateUsed(response, "evas/eva_detail.html")
