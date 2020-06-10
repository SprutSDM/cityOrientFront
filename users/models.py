from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_quest_maker(self, username: str, password: str):
        if username.lower().startswith("team"):
            ValueError("The username field must not starts with 'team'.")
        user = self.model(username=username)
        user.set_password(password)
        user.is_quest_maker = True
        user.save()
        return user

    def create_team(self):
        user = self.model(username=f"team{self.model.objects.count() + 1}")
        user.set_password(self.make_random_password(length=8))
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    is_quest_maker = models.BooleanField(
        'is_quest_maker',
        default=False
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    objects = UserManager()

    def __str__(self):
        return self.username
