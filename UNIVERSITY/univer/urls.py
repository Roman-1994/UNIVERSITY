from django.urls import path
from univer import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'direction_training', views.DirectionTrainingViewSet)
router.register(r'academic_discipline', views.AcademicDisciplineViewSet)
router.register(r'student', views.CRUDStudentsViewSet)

urlpatterns = [
    path('up_student/<int:pk>', views.StudentToGroupViewSet.as_view({'put': 'update'})),
    path('up_tutor/<int:pk>', views.TutorToDirectionTrainingViewSet.as_view({'put': 'update'})),
    path('report/', views.ReportViewSet.as_view({'get': 'get'}))
]
