from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Resgatador, Animal

# Create your views here.

def vitrine(request):
    lista_animais = Animal.objects.order_by("-data_atualizacao")[:5]
    template = loader.get_template("vitrine/vitrine.html")
    context = {
            "lista_animais": lista_animais,
    }
    return HttpResponse(template.render(context, request))

