from rest_framework.viewsets import ModelViewSet
from apis.serializers import ClassroomSerializer
from apis.models import Classroom
from apis.filters import ClassroomFilter


class ClassroomViewSet(ModelViewSet):
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()
    filterset_class = ClassroomFilter
