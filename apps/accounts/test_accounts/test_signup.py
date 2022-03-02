# apps/accounts/test_signup.py

# import get_user_model in first from/import line looks to the AUTH_USER_MODEL config \
# in settings/settings.py
# it enforces the idea of making one single reference to the custom user model rather \
# than directly referring to it all over the project

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve


class SignUpTests(TestCase):

    username = "newuser"
    email = "newuser@email.com"

    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "I should not be on this page")

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
