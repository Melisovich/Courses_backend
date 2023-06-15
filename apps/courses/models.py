from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from apps.users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def _str_(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    instructor = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def _str_(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def _str_(self):
        return self.title


class Review(models.Model):
    course = models.ForeignKey(Course, verbose_name='Курс', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, verbose_name='Студент', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    rating = models.PositiveIntegerField(
        verbose_name='Рейтинг',
        validators=[
            MinValueValidator(1, message='Рейтинг должен быть от 1 до 10.'),
            MaxValueValidator(10, message='Рейтинг должен быть от 1 до 10.')
        ]
    )

    def update_rating(self):
        reviews = self.review_set.all()
        if reviews.exists():
            total_rating = sum(review.rating for review in reviews)
            self.rating = total_rating / reviews.count()
        else:
            self.rating = None
        self.save()

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'Review by {self.user.username} on {self.course.title}'