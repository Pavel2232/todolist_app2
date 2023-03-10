from django.contrib.auth.base_user import AbstractBaseUser

from core.managers import UserManager
from django.db import models


class User(AbstractBaseUser):
    username = models.CharField(max_length=200, unique=True, verbose_name="Никнейм")
    first_name = models.CharField(max_length=200, null=True,verbose_name="Имя")
    last_name = models.CharField(max_length=200, null=True,verbose_name="Фамилия")
    email = models.EmailField(max_length=255, null=False,verbose_name="Почта")
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    def has_perm(self) -> bool:
        return True

    def has_module_perms(self) -> bool:
        return True

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
