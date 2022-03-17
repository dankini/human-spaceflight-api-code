# apps/astronauts/Test_astronauts/test_astronaut.py

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from apps.astronauts.views import Astronaut


class AstronautTests(TestCase):
    # https://docs.djangoproject.com/en/4.0/topics/testing/tools/#django.test.TestCase.setUpTestData
    @classmethod
    def setUpTestData(cls):
        # Commented out lines earmarked as possibly required for future use
        cls.astronaut = Astronaut.objects.create(
            first_name="Test astronaut firstname",
            middle_name="Test astronaut middlename",
            nick_name="Test astronaut nickname",
            last_name="Test astronaut lastname",
            birth_date="1930-03-07",
            birth_town_city="Test town",
            birth_state="Test state",
            birth_country="Test country",
            death_date="2022-03-07",
            resting_place="Test resting place",
            # alma_mater_list=,
            # occupation_list=,
            rank_attained="Test rank attained",
            service_branch="Test service branch",
            nationality="Test nationality",
            first_time_in_space_date="1965-03-07",
            total_duration_space_secs="00:00:01",
            # mission_list=,
            # insignia_list=,
            # selection_group=,
            # total_eva=,
            # total_eva_duration_space_secs=,
            # award_list=,
            retirement_date="1972-03-07",
            # image_photo=,
            # image_signature=,
            wikipedia_bio_website="www.testastronaut.com",
        )

    def test_astronaut_content(self):
        self.assertEqual(f"{self.astronaut.first_name}", "Test astronaut firstname")
        self.assertEqual(f"{self.astronaut.middle_name}", "Test astronaut middlename")
        self.assertEqual(f"{self.astronaut.nick_name}", "Test astronaut nickname")
        self.assertEqual(f"{self.astronaut.last_name}", "Test astronaut lastname")
        self.assertEqual(f"{self.astronaut.birth_date}", "1930-03-07")
        self.assertEqual(f"{self.astronaut.birth_town_city}", "Test town")
        self.assertEqual(f"{self.astronaut.birth_state}", "Test state")
        self.assertEqual(f"{self.astronaut.birth_country}", "Test country")
        self.assertEqual(f"{self.astronaut.death_date}", "2022-03-07")
        self.assertEqual(f"{self.astronaut.resting_place}", "Test resting place")
        # self.assertEqual(f"{self.astronaut.alma_mater_list}", "")
        # self.assertEqual(f"{self.astronaut.occupation_list}", "")
        self.assertEqual(f"{self.astronaut.rank_attained}", "Test rank attained")
        self.assertEqual(f"{self.astronaut.service_branch}", "Test service branch")
        self.assertEqual(f"{self.astronaut.nationality}", "Test nationality")
        self.assertEqual(f"{self.astronaut.first_time_in_space_date}", "1965-03-07")
        self.assertEqual(f"{self.astronaut.total_duration_space_secs}", "00:00:01")
        # self.assertEqual(f"{self.astronaut.mission_list}", "")
        # self.assertEqual(f"{self.astronaut.insignia_list}", "")
        # self.assertEqual(f"{self.astronaut.selection_group}", "")
        # self.assertEqual(f"{self.astronaut.total_eva}", "")
        # self.assertEqual(f"{self.astronaut.total_eva_duration_space_secs}", "")
        # self.assertEqual(f"{self.astronaut.award_list}", "")
        self.assertEqual(f"{self.astronaut.retirement_date}", "1972-03-07")
        # self.assertEqual(f"{self.astronaut.image_photo}", "")
        # self.assertEqual(f"{self.astronaut.image_signature}", "")
        self.assertEqual(
            f"{self.astronaut.wikipedia_bio_website}", "www.testastronaut.com"
        )

    def test_astronaut_list_view(self):
        response = self.client.get(reverse("astronaut_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test astronaut lastname")
        self.assertTemplateUsed(response, "astronauts/astronaut_list.html")

    def test_astronaut_detail(self):
        response = self.client.get(self.astronaut.get_absolute_url())
        no_response = self.client.get("/astronaut/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Test astronaut lastname")
        self.assertTemplateUsed(response, "astronauts/astronaut_detail.html")
