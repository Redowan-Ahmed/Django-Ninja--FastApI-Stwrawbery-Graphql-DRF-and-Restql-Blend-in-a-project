from ninja import schema, ModelSchema
from portfolio.models import Project
from ninja.orm import create_schema

#way 2
class ProjectSchema(ModelSchema):
    class Meta:
        model = Project
        fields = ['id', 'created_at']
        # fields_optional  = ['id']


#way 3
#ProjectSchema2 = create_schema(Project , optional_fields=['id'])
ProjectSchema2 = create_schema(Project)