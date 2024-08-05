from rest_framework import serializers
from .models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'members']


class TaskSerializer(serializers.ModelSerializer):
    project_name = serializers.StringRelatedField(source='project')
    # assiged_to_username = serializers.StringRelatedField(source='user')
    assiged_to_username = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date',
                  'completed', 'project_name', 'assiged_to_username']

    def get_assiged_to_username(self, obj):
        # Access the 'assigned_to' field and return the username
        return obj.assiged_to.username if obj.assiged_to else None
