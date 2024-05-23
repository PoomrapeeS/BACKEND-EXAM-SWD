from rest_framework.viewsets import ModelViewSet
from apis.serializers import StudentSerializer
from apis.models import Student
from apis.filters import StudentFilter


class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    filterset_class = StudentFilter
