from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg

from apps.users.models import CustomUser


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    instructor = models.ForeignKey('users.UserProfile', verbose_name='Инструктор', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Создан в', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено в', auto_now=True)

    def calculate_rating(self):
        rating = self.review_set.aggregate(avg_rating=Avg('rating'))['avg_rating']
        if rating is not None:
            return round(rating, 2)
        else:
            return None

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='Курс', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    content = models.TextField(verbose_name="Содержание")

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.title


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'), (2, '2'),
        (3, '3'), (4, '4'),
        (5, '5'), (6, '6'),
        (7, '7'), (8, '8'),
        (9, '9'), (10, '10'),
    )
    course = models.ForeignKey(Course, verbose_name='Курс', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, verbose_name='Студент', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(verbose_name='Создан в', auto_now_add=True)
    rating = models.PositiveIntegerField(
        verbose_name='Рейтинг',
        choices=RATING_CHOICES,
        validators=[
            MinValueValidator(1, message='Рейтинг должен быть от 1 до 10.'),
            MaxValueValidator(10, message='Рейтинг должен быть от 1 до 10.')
        ]
    )

    def update_rating(self):
        reviews = self.course.review_set.all()
        if reviews.exists():
            total_rating = sum(review.rating for review in reviews)
            self.course.rating = total_rating / reviews.count()
        else:
            self.course.rating = None
        self.course.save()

    def __str__(self):
        return f'Review by {self.user.username} on {self.course.title}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        