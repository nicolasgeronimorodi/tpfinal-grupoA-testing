from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import URLForm
from .models import URLAlias

# Create your views here.

def index(request):


    if request.method == "POST":
        # Se puede acceder a la informacion del POST de forma
        # manual
        # request.POST["nombre"])
        form = URLForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("El formulario es invalido") 
    
    form = URLForm()

    ctx  = {"title": "Bienvenido al url alias", "form": form}
	

    return render(request, "urlalias/home.html", ctx)

def resolve_alias(request, alias):
    resultado = URLAlias.objects.get(alias=alias)

    # return HttpResponse(f"La URL para el alias {alias} es {resultado.fullurl}")
    return HttpResponseRedirect(resultado.fullurl) 

