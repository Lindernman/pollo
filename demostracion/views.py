# import Http Response from django
from django.shortcuts import  redirect, render

from demostracion.models import Person


def index(request):

    if request.method == 'POST':
        nombre = request.POST['nombre']
        Person.objects.create(nombre=nombre)
        data = Person.objects.values()
        context = {
            'personas': data
        }
        return render(request, "test.html", context)
    else:
        data = Person.objects.values()
        context = {
            'personas': data
        }
        return render(request, "test.html", context)


def eliminar_usuario(request, id):

    Person.objects.filter(id=id).delete()
    return redirect("pagina_principal")
