from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, verbose_name='Группы', related_name='custom_users', related_query_name='custom_user')
    user_permissions = models.ManyToManyField(Permission, verbose_name='Разрешения пользователя', blank=True)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, verbose_name='Студент', on_delete=models.CASCADE)
    bio = models.TextField(verbose_name='Био')
    avatar = models.ImageField(verbose_name='Аватар', upload_to='avatars/')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    created_at = models.DateTimeField(verbose_name='Создан в', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено в', auto_now=True)
    instructor = models.BooleanField(verbose_name='Инструктор', default=False)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Enrollment(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='Студент', on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', verbose_name='Курс', on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(verbose_name='Дата регистрации', auto_now_add=True)

    class Meta:
        verbose_name = 'Регистрация'
