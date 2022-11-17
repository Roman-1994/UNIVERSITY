from django.db import models
from django.contrib.auth.models import AbstractUser


class UserTutorStudent(AbstractUser):
    """Модель User"""
    is_tutor = models.BooleanField(default=False, verbose_name='Является куратором')
    tutor = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Куратор', null=True, blank=True,
                              related_name='user_tutors')
    phone = models.CharField(max_length=20, verbose_name='Телефон', null=True, blank=True)
    age = models.SmallIntegerField(verbose_name='Возраст', null=True, blank=True)
    study_group = models.ForeignKey('StudyGroup', on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='students', verbose_name="Учебная группа")
    direction_training = models.ForeignKey('DirectionTraining', on_delete=models.SET_NULL, null=True, blank=True,
                                           related_name='tutors', verbose_name="Направление подготовки")
    gender = models.ForeignKey('Gender', on_delete=models.SET_NULL, verbose_name='Пол', default=1,
                               null=True, blank=True, related_name='genders')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Gender(models.Model):
    """Модель пола"""
    gender = models.CharField(max_length=20, verbose_name='Пол')

    def __str__(self):
        return self.gender

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'


class DirectionTraining(models.Model):
    """Модель направлений подготовок"""
    title = models.CharField(max_length=50, verbose_name='Наименование направления')
    content = models.TextField(max_length=5000, verbose_name='Описание направления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Направление подготовки'
        verbose_name_plural = "Направления подготовок"
        ordering = ('title',)


class StudyGroup(models.Model):
    """Модель учебных групп"""
    title = models.CharField(max_length=10, verbose_name='Наименование группы')
    direction_training = models.ForeignKey(DirectionTraining, on_delete=models.CASCADE, related_name='stud_gr',
                                           verbose_name='Направление подготовки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Учебная группа'
        verbose_name_plural = 'Учебные группы'
        ordering = ('direction_training', 'title')


class AcademicDiscipline(models.Model):
    """Модель учебных дисциплин"""
    title = models.CharField(max_length=20, verbose_name='Учебная дисциплина')
    content = models.TextField(max_length=5000, verbose_name='Описание предмета')
    direction_training = models.ForeignKey(DirectionTraining, on_delete=models.CASCADE, related_name='academ_dis',
                                           verbose_name='Направление подготовки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Учебная дисциплина'
        verbose_name_plural = 'Учебные дисциплины'
        ordering = ('direction_training', 'title')
