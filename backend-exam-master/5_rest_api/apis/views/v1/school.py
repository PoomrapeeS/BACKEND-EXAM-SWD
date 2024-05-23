from rest_framework.viewsets import ModelViewSet
from apis.serializers import SchoolSerializer
from apis.models import School
from apis.filters import SchoolFilter


class SchoolViewSet(ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    filterset_class = SchoolFilter
