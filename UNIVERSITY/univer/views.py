
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from univer.service import TutorPermissions, AdminPermissions
from univer.serializers import *
from univer.task import report_exel


class CRUDStudentsViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          GenericViewSet):
    """CRUD студентов"""
    queryset = UserTutorStudent.objects.filter(is_tutor=False)
    serializer_class = StudentsSerializer
    permission_classes = [TutorPermissions]


class DirectionTrainingViewSet(viewsets.ModelViewSet):
    """CRUD направлений подготовок"""
    serializer_class = DirectionTrainingSerializer
    queryset = DirectionTraining.objects.all()
    permission_classes = [AdminPermissions]


class AcademicDisciplineViewSet(viewsets.ModelViewSet):
    """CRUD учебных дисциплин"""
    serializer_class = AcademicDisciplineSerializer
    queryset = AcademicDiscipline.objects.all()
    permission_classes = [AdminPermissions]


class StudentToGroupViewSet(viewsets.ViewSet):
    """Зачисление студентов в группу"""
    permission_classes = [TutorPermissions]

    def update(self, request, pk=None):
        students_list = request.data['users']
        serializer = StudentToGroupSerializer(data={'users': students_list, 'study_group_id': pk})
        serializer.is_valid(raise_exception=True)
        study_group = StudyGroup.objects.get(id=pk)
        direction_training = DirectionTraining.objects.get(stud_gr=study_group)
        UserTutorStudent.objects.filter(id__in=students_list).\
            update(study_group_id=pk,
                   tutor_id=UserTutorStudent.objects.get(direction_training=direction_training),
                   direction_training_id=direction_training)
        return Response({})


class TutorToDirectionTrainingViewSet(viewsets.ViewSet):
    """Закрепление куратора за направлением подготовки"""
    permission_classes = [AdminPermissions]

    def update(self, request, pk=None):
        tutor = request.data['users']
        serializer = TutorToDirectionTrainingSerializer(data={'users': tutor, 'direction_training_id': pk})
        serializer.is_valid(raise_exception=True)
        tutor_direction_training = UserTutorStudent.objects.get(id=tutor)
        tutor_direction_training.direction_training_id = pk
        tutor_direction_training.save()
        return Response({})


class ReportViewSet(viewsets.ViewSet):
    """Создание отчета"""
    def get(self, request):
        report_exel.delay()
        return Response('Отчет сделан')

