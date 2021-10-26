from django import views
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from .forms import URLForm2
from .models import URLAlias, TestURLAlias
import nanoid

import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


_NANO_DICT = "abcdefz-"

@method_decorator(csrf_exempt, name='dispatch')
class Api2(views.View):
    model=TestURLAlias
    def post(self, request):
        data=json.loads(request.body.decode("utf-8")   )
        print(f" data es {data} y es de tipo {type(data)}"   )
        url=data.get('url')
        print(f"url es {url} y es de tipo {type(url)}")
        
        
        Url=TestURLAlias(fullurl=url)
        alias=nanoid.generate(alphabet=_NANO_DICT, size=5)
        Url.alias=alias
        Url.save()

        response={"alias": alias}
        print(f"response es {response}")
        return JsonResponse(response, status=201)




"""



def index(request):


    if request.method == "POST":
        # Se puede acceder a la informacion del POST de forma
        form = URLForm2(request.POST)
        if form.is_valid():
            fullurl = form.cleaned_data.get("fullurl")
            url = URLAlias(fullurl=fullurl)
            alias = nanoid.generate(size=5)
            url.alias=alias
            url.save()
            ctx  = {"title": "Bienvenido al url alias", "url": fullurl, "alias": alias}
            return render(request, "urlalias/registrado.html", ctx)
        else:
            return HttpResponse("El formulario es invalido") 
    
    form = URLForm2()

    ctx  = {"title": "Bienvenido al url alias", "form": form}
	

    return render(request, "urlalias/home.html", ctx)



//def resolve_alias(request, alias):
//    resultado = URLAlias.objects.get(alias=alias)
//    resultado.visitas += 1
//    resultado.save()
//
//    # return HttpResponse(f"La URL para el alias {alias} es {resultado.fullurl}")
//    return HttpResponseRedirect(resultado.fullurl) 

"""