import strawberry
from strawberry_django.optimizer import DjangoOptimizerExtension

from .types import Contact



class Query:
    contacts: list[Contact] = strawberry.django.field()


schema = strawberry.Schema(
    query=Query,
    extensions=[
        DjangoOptimizerExtension,  # not required, but highly recommended
    ],

)
