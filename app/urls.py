from django.urls import path

from app.views import ClientsAPIView, ClientProjectsAPIView, ProjectsAPIView

urlpatterns = [
    path("clients/", ClientsAPIView.as_view(), name="clients"),
    path("clients/<int:id>/", ClientsAPIView.as_view(), name="client-id"),
    path("clients/<int:id>/projects/", ClientProjectsAPIView.as_view(), name="client-projects"),
    path("projects/", ProjectsAPIView.as_view(), name="projects"),
]