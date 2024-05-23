from rest_framework.viewsets import ModelViewSet
from apis.serializers import TeacherSerializer
from apis.models import Teacher
from apis.filters import TeacherFilter


class TeacherViewSet(ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    filterset_class = TeacherFilter
