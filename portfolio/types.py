import strawberry
import strawberry.django
from strawberry import auto

from . import models

@strawberry.django.type(models.Contact)
class Contact:
    id: auto
    email: auto
    full_name: auto
    massage: auto
    phoneNumber: auto