from ninja import NinjaAPI
from typing import List
from portfolio.models import Project
from .schema import ProjectSchema, ProjectSchema2
from django.shortcuts import get_object_or_404

route = NinjaAPI()


@route.get("/add/{id}")
def add(request, id: int, a: int, b: int):
    return {"result": a + b, 'id': id}


@route.get("/projects", response=List[ProjectSchema2])
def projects(request):
    projects = Project.objects.all()

    return projects


@route.get('/project/{id}', response=ProjectSchema2)
def project(request, id: str):
    try:
        project = get_object_or_404(Project, pk=id)
        return project
    except Exception as e:
        return {
            'error': e
        }
