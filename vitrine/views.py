from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
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

def detalhes(request, id):
    animal = get_object_or_404(Animal, pk=id)
    data = {
            'nome': animal.nome,
            'peso': float(animal.peso),
            'idade_aproximada': animal.idade_aproximada,
            'sexo': animal.get_sexo_display(),
            'microchip': animal.microchip,
            'especie': animal.especie,
            'porte': animal.get_porte_display(),
            'raca': animal.raca,
            'estado': animal.estado,
            'cidade': animal.cidade,
            'sobre_o_pet': animal.sobre_o_pet,
            'adotado': animal.adotado,
            'foto': animal.foto.url,
            'resgatador': animal.resgatador.nome,
    }
    return JsonResponse(data)
