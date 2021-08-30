from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class TimeFocusUsers(AbstractUser):
    avatar = models.ImageField('Аватар', blank=True, upload_to='avatars')
    b_date = models.DateField('Дата рождения', null=True)
    user_info = models.TextField('Описание человека от его лица\статус', blank=True)
    instagram = models.URLField('Ccылка на инсту', blank=True)
    city = models.TextField('Город')

