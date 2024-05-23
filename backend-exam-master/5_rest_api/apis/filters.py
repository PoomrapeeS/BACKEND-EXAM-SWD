from django_filters import FilterSet, filters
from apis.models import School, Classroom, Teacher, Student


# code here
class SchoolFilter(FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = School
        fields = ["name"]


class ClassroomFilter(FilterSet):
    school = filters.CharFilter(field_name="school__name", lookup_expr="icontains")

    class Meta:
        model = Classroom
        fields = ["school"]


class TeacherFilter(FilterSet):
    class Meta:
        model = Teacher
        fields = {
            "school__name": ["icontains"],
            "name": ["icontains"],
            "surname": ["icontains"],
            "classroom": ["exact"],
            "gender": ["exact"],
        }


class StudentFilter(FilterSet):
    class Meta:
        model = Student
        fields = {
            "school__name": ["icontains"],
            "name": ["icontains"],
            "surname": ["icontains"],
            "classroom": ["exact"],
            "gender": ["exact"],
        }
