from rest_framework import serializers
from apis.models import School, Classroom, Teacher, Student


# code here
class SchoolSerializer(serializers.ModelSerializer):
    detail = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ["id", "name", "abbreviation", "address", "detail"]

    def get_detail(self, obj):
        return {
            "number_of_classroom": obj.classroom_count(),
            "number_of_teacher": obj.teacher_count(),
            "number_of_student": obj.student_count(),
        }


class ClassroomSerializer(serializers.ModelSerializer):
    detail = serializers.SerializerMethodField()

    class Meta:
        model = Classroom
        fields = ["id", "year", "room", "school", "detail"]

    def get_detail(self, obj):
        return {
            "school": obj.school.name,
            "list_of_teachers": obj.teachers(),
            "list_of_students": obj.students(),
        }


class TeacherSerializer(serializers.ModelSerializer):
    detail = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ["id", "name", "surname", "gender", "classroom", "school", "detail"]

    def validate(self, data):
        for classroom in data["classroom"]:
            if classroom.school != data["school"]:
                raise serializers.ValidationError(
                    "The school of the teacher must be the same as the school of their classroom."
                )
        return data

    def get_detail(self, obj):
        return {
            "school": obj.school.name,
            "classroom": [
                f"{classroom.year}/{classroom.room}"
                for classroom in obj.classroom.all()
            ],
        }


class StudentSerializer(serializers.ModelSerializer):
    detail = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ["id", "name", "surname", "gender", "classroom", "school", "detail"]

    def validate(self, data):
        if data["classroom"].school != data["school"]:
            raise serializers.ValidationError(
                "The school of the student must be the same as the school of their classroom."
            )
        return data

    def get_detail(self, obj):
        return {
            "school": obj.school.name,
            "classroom": f"{obj.classroom.year}/{obj.classroom.room}",
        }
