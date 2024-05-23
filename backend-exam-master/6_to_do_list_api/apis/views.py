from rest_framework.viewsets import ModelViewSet
from apis.serializers import CategorySerializer, TaskSerializer
from apis.models import Category, Task
from apis.filters import CategoryFilter, TaskFilter


# Create your views here.
class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filterset_class = CategoryFilter


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filterset_class = TaskFilter
