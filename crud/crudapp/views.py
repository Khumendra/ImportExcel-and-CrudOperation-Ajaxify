from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from crudapp.models import CrudUser
from .resources import CrudResource
from django.contrib import messages
from tablib import Dataset


def simple_upload(request):
    if request.method == "POST":
        person_resource = CrudResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']

        if not new_person.name.endswith('xlsx'):
            messages.info(request, 'Wrong format  supports xlsx format')
            return render(request, 'upload.html')

        imported_data = dataset.load(new_person.read(), format='xlsx')
        for data in imported_data:
            value = CrudUser(
                data[0],
                data[1],
                data[2],
                data[3],
            )
            value.save()
    return render(request, 'upload.html')


# Create your views here.
def index(request):
    return render(request, 'index.html')


class CrudView(ListView):
    model = CrudUser
    template_name = 'crudapp/crud.html'
    context_object_name = 'users'


# Create and Read User Django Ajax

from django.views.generic import View
from django.http import JsonResponse
from .models import CrudUser


class CreateCrudUser(View):
    def get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.create(
            name=name1,
            address=address1,
            age=age1
        )
        user = {'id': obj.id, 'name': obj.name, 'address': obj.address, 'age': obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)


# Update User Django Ajax
class UpdateCrudUser(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()

        user = {'id': obj.id, 'name': obj.name, 'address': obj.address, 'age': obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)


# Delete User Django Ajax
class DeleteCrudUser(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

