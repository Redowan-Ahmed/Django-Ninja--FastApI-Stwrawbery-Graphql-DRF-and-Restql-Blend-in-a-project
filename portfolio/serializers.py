from rest_framework import serializers
from .models import WorkExperience, SocialMedia, Contact, Project, Skill
from django_restql.mixins import DynamicFieldsMixin


class WorkExperienceSerializer(DynamicFieldsMixin ,serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'


class SocialMediaSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'


class ContactSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ProjectSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class SkillSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
