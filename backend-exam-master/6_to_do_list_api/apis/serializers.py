from rest_framework import serializers
from apis.models import Category, Task


# code here
class CategorySerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ["id", "category_name", "tasks"]

    def get_tasks(self, obj):
        tasks = obj.tasks()
        return TaskSerializer(tasks, many=True).data


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
