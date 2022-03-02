# apps/accounts/forms.py

# This allows us to make/modify users from within our project itself aswell as via the admin app.
# import get_user_model in first from/import line looks to the AUTH_USER_MODEL config \
# in settings/settings.py
# it enforces the idea of making one single reference to the custom user model rather \
# than directly referring to it all over the project

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    """Class docstring."""

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    """Class docstring."""

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )
