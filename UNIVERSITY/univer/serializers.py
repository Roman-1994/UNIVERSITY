from rest_framework import serializers
from univer.models import *


class StudentsSerializer(serializers.ModelSerializer):
    """Сериализатор студентов"""
    class Meta:
        model = UserTutorStudent
        fields = ('username', 'first_name', 'last_name', 'gender', 'phone', 'age', 'password')


class DirectionTrainingSerializer(serializers.ModelSerializer):
    """Сериализатор направлений подготовок"""
    class Meta:
        model = DirectionTraining
        fields = '__all__'


class AcademicDisciplineSerializer(serializers.ModelSerializer):
    """Сериализатор учебных дисциплин"""
    class Meta:
        model = AcademicDiscipline
        fields = '__all__'


class StudentToGroupSerializer(serializers.Serializer):
    """Сериализатор зачисления студентов в группу"""
    users = serializers.ListField()
    study_group_id = serializers.IntegerField()

    def validate(self, data):
        group = StudyGroup.objects.get(id=data['study_group_id'])
        count_stud = group.students.all().count() + len(data['users'])
        if count_stud > 3:
            raise serializers.ValidationError({'users': ['Группа переполнена']})
        return data


class TutorToDirectionTrainingSerializer(serializers.Serializer):
    """Сериализатор закрепления кураторов за направлением"""
    users = serializers.IntegerField()
    direction_training_id = serializers.IntegerField()

    def validate(self, data):
        direction_training = DirectionTraining.objects.get(id=data['direction_training_id'])
        tutor = direction_training.tutors.all().count()
        if tutor == 1:
            raise serializers.ValidationError({'users': ['У направления не может быть больше одного куратора']})
        return data
