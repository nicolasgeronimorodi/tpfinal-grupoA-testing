from django.shortcuts import render
from django.http import HttpResponse
from .forms import URLForm

# Create your views here.

def index(request):


    if request.method == "POST":
        # Se puede acceder a la informacion del POST de forma
        # manual
        # request.POST["nombre"])
        form = URLForm(request.POST)
        if form.is_valid():
            return HttpResponse(f"El formulario es valido") 
        else:
            return HttpResponse("El formulario es invalido") 
    
    form = URLForm()

    ctx  = {"title": "Bienvenido al url alias", "form": form}
	

    return render(request, "urlalias/home.html", ctx)
