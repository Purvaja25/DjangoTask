from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView
from app.models import Client, Project
from app.serializers import (
    ClientSerializer, 
    ClientProjectResponseSerializer, 
    ProjectCreateSerializer,
    ProjectListSerializer
)


# Create your views here.

class ClientsAPIView(APIView):

    def get(self, request, id=None):
        if id:
            client_obj = get_object_or_404(Client, id=id)
            return Response(ClientProjectResponseSerializer(client_obj).data)
        else:
            client_qs = Client.objects.all()
            return Response(ClientSerializer(client_qs, many=True).data)

    def post(self, request, *args, **kwargs):
        payload = request.data.copy()
        payload['created_by'] = request.user.id
        payload['updated_by'] = request.user.id
        serializer = ClientSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        if not id:
            return Response({"error": "Client ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        payload = request.data.copy()
        payload['updated_by'] = request.user.id
        client_obj = get_object_or_404(Client, id=id)
        serializer = ClientSerializer(client_obj, data=payload, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):        
        client_obj = get_object_or_404(Client, id=id)
        client_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClientProjectsAPIView(APIView):
    
    def post(self, request, id=None):
        if not id:
            return Response({"error": "Client ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        client_obj = get_object_or_404(Client, id=id)

        data = request.data.copy()
        data['client'] = client_obj.id
        data['created_by'] = request.user.id
        data['updated_by'] = request.user.id
        
        serializer = ProjectCreateSerializer(data=data)
        if serializer.is_valid():
            project = serializer.save()
            
            response_data = ProjectListSerializer(project).data
            
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectsAPIView(APIView):
    
    def get(self, request):
        if request.user.is_authenticated:
            projects = Project.objects.filter(users=request.user)
            serializer = ProjectListSerializer(projects, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Authentication is required"}, status=status.HTTP_401_UNAUTHORIZED)