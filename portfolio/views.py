from rest_framework import viewsets
from .models import Contact, Project, Skill, SocialMedia, WorkExperience
from .serializers import ContactSerializer, ProjectSerializer, SkillSerializer, SocialMediaSerializer, WorkExperienceSerializer
from rest_framework.permissions import BasePermission


class WorkExperianceView(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all().order_by('-created_at')
    serializer_class = WorkExperienceSerializer
    http_method_names = ['get']

class SocialMediaView(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.all().order_by('-created_at')
    serializer_class = SocialMediaSerializer
    http_method_names = ['get']

class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('-created_at')
    serializer_class = ContactSerializer
    http_method_names = ['post']


class ProjectsView(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    http_method_names = ['get']


class SkillsView(viewsets.ModelViewSet):
    queryset = Skill.objects.all().order_by('-created_at')
    serializer_class = SkillSerializer
    http_method_names = ['get']
