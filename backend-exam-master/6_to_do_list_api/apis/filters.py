from django_filters import FilterSet, filters
from apis.models import Category, Task


class CategoryFilter(FilterSet):
    category_name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Category
        fields = ["category_name"]


class TaskFilter(FilterSet):
    class Meta:
        model = Task
        fields = {
            "title": ["icontains"],
            "completed": ["exact"],
            "category": ["exact"],
        }
