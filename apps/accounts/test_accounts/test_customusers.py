# apps/accounts/test_customuser.py

# import get_user_model in first from/import line looks to the AUTH_USER_MODEL config \
# in settings/settings.py
# it enforces the idea of making one single reference to the custom user model rather \
# than directly referring to it all over the project

from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            email="testuser@email.com",
            password="testpass123",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superusertest",
            email="superusertest@email.com",
            password="testpass123",
        )
        self.assertEqual(admin_user.username, "superusertest")
        self.assertEqual(admin_user.email, "superusertest@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
