from django.shortcuts import render

# Create your views here.

def index(request):

    ctx  = {"title": "Bienvenido al url alias"}

    return render(request, "urlalias/home.html", ctx)
