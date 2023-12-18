from django.urls import include, path
from rest_framework.routers import DefaultRouter
from portfolio.views import WorkExperianceView, SocialMediaView, ContactView, ProjectsView, SkillsView
from ninjaapi.api import route

router = DefaultRouter()
router.register('work-experainces', WorkExperianceView,
                basename="work-experience")
router.register('social-medias', SocialMediaView, basename="social-media")
router.register('skills', SkillsView, basename="skills")
router.register('projects', ProjectsView, basename="projects")
router.register('contact', ContactView, basename="contact")


urlpatterns = [
    #this one for DRF
    path('', include(router.urls)),

    #this one for Ninja Fast Api
    path('napi/', route.urls)
]
