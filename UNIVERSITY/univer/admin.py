from django.contrib import admin
from univer.models import *


class UserTutorStudentAdmin(admin.ModelAdmin):
    """Админка пользователей"""
    list_display = ('username', 'phone', 'is_tutor', 'tutor')
    fields = ('username', 'is_staff', 'is_tutor', 'tutor', 'first_name', 'last_name', 'study_group',
              'direction_training', 'phone', 'age', 'gender', 'password')


class DirectionTrainingAdmin(admin.ModelAdmin):
    """Админка направлений подготовок"""
    list_display = ('title',)
    fields = ('title', 'content')


class StudyGroupAdmin(admin.ModelAdmin):
    """Админка учебных групп"""
    list_display = ('title', 'direction_training')
    fields = ('title', 'direction_training')


class AcademicDisciplineAdmin(admin.ModelAdmin):
    """Админка учебных дисциплин"""
    list_display = ('title', 'direction_training')
    fields = ('title', 'direction_training', 'content')


class GenderAdmin(admin.ModelAdmin):
    """Админка пола"""
    list_display = ('gender', )
    fields = ('gender', )


admin.site.register(UserTutorStudent, UserTutorStudentAdmin)
admin.site.register(DirectionTraining, DirectionTrainingAdmin)
admin.site.register(StudyGroup, StudyGroupAdmin)
admin.site.register(AcademicDiscipline, AcademicDisciplineAdmin)
admin.site.register(Gender, GenderAdmin)
