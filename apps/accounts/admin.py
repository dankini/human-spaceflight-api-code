# apps/accounts/admin.py

# import get_user_model in first from/import line looks to the AUTH_USER_MODEL config \
# in settings/settings.py
# it enforces the idea of making one single reference to the custom user model rather \
# than directly referring to it all over the project

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    """Class docstring."""

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
