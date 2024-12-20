from django.apps import apps
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import AbstractBaseUser

from myapp.account.base import BaseModel

from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models


class AccountManager(UserManager):
    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields['is_staff'] = extra_fields['is_superuser'] = True
        return self._create_user(username, password, **extra_fields)


class Account(AbstractBaseUser, BaseModel, PermissionsMixin):  # Add PermissionsMixin here
    """
    Asosiy User modeli
    """
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    middle_name = models.CharField(_("middle name"), max_length=150, blank=True)
    is_staff = models.BooleanField(default=False)  # Add this field
    is_superuser = models.BooleanField(default=False)  # Add this field
    date_joined = models.DateTimeField(default=timezone.now)  # Optional field

    def __str__(self):
        return f'Username :{self.username}'

    objects = AccountManager()

    USERNAME_FIELD = "username"

    class Meta:
        verbose_name = _("account")
        verbose_name_plural = _("accounts")
