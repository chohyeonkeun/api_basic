from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): # 클래스 이름 다른 것으로 작성해도 무방하다.
    message = models.TextField(blank=True)
    profile = models.ImageField(upload_to='user_images/profile/%Y/%m/%d', blank=True)
