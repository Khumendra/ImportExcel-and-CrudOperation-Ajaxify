from import_export import resources
from .models import CrudUser


class CrudResource(resources.ModelResource):
    class meta:
        model = CrudUser
