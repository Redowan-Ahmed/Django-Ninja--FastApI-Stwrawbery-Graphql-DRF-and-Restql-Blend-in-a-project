from rest_framework import viewsets
from rest_framework.response import Response
from .models import Contact, Project, Skill, SocialMedia, WorkExperience

from .serializers import ContactSerializer, ProjectSerializer, SkillSerializer, SocialMediaSerializer, WorkExperienceSerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class WorkExperianceView(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all().order_by('-created_at')
    serializer_class = WorkExperienceSerializer
    http_method_names = ['get']

    @method_decorator(cache_page(60*60))
    def list(self, request, format=None):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SocialMediaView(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.all().order_by('-created_at')
    serializer_class = SocialMediaSerializer
    http_method_names = ['get']

    @method_decorator(cache_page(60*60))
    def list(self, request, format=None):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('-created_at')
    serializer_class = ContactSerializer
    http_method_names = ['post']


class ProjectsView(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    http_method_names = ['get']

    @method_decorator(cache_page(60*60))
    def list(self, request, format=None):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SkillsView(viewsets.ModelViewSet):
    queryset = Skill.objects.all().order_by('-created_at')
    serializer_class = SkillSerializer
    http_method_names = ['get']

    @method_decorator(cache_page(60*60))
    def list(self, request, format=None):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
