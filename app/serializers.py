from rest_framework.serializers import ModelSerializer

from app.models import Client, Project


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class ClientProjectResponseSerializer(ModelSerializer):
    projects = ProjectSerializer(many=True, required=False)
    
    class Meta:
        model = Client
        fields = "__all__"

class ProjectCreateSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class ProjectListSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'created_at', 'created_by']
