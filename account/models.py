from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone
# from rest_framework_simplejwt.tokens import RefreshToken
import uuid
import os


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('The given email must be set')

        # e-mail addressの正規化
        email = self.normalize_email(email)
        user = self.model(email=email)
        # passwordをハッシュ化してから設定
        user.set_password(password)
        # self._dbは、settings.pyで設定したdefaultのデータベース
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        # user.is_verified = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=50, unique=True)
    # ユーザー登録の確認メールのURLが押されると、is_verifiedがTrueになる。
    # is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()
    # 登録時にユーザー名の代わりにメールアドレスを利用する
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    # def tokens(self):
    #     refresh = RefreshToken.for_user(self)
    #     return {
    #         'refresh': str(refresh),
    #         'access': str(refresh.access_token)
    #     }