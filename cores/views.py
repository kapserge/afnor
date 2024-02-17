import json
import logging

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from .forms import ObfuscatedForm
from .models import Obfuscated
from django.http import HttpResponse, Http404 
######## GET ALL LIST
@require_http_methods(['GET'])
def Obfuscated_list(request):
    alldatas = Obfuscated.objects.all()
    data = [obf.to_dict() for obf  in alldatas]
    return JsonResponse({'data': data})

######## GET DETAIL
@require_http_methods(['GET'])
def Obfuscated_detail(request, pk):
    try:
    # try something
        Obfuscated_one = Obfuscated.objects.get(pk=pk)
        data = Obfuscated_one.to_dict()
        return JsonResponse({'data': data})
    except Obfuscated.DoesNotExist:
        raise Http404("The requested Obfuscated does not exist.") 
        

######## INSERT
@csrf_exempt
@require_http_methods(['POST'])
def Obfuscated_create(request):
    form = ObfuscatedForm(request.POST or None)

    if request.POST:
        # Données obtenues par le formulaire.
        if form.is_valid():
            Obf = form.save()

    elif request.body:
        # Données obtenues via json.
        data = json.loads(request.body)
        Obf= Obfuscated.objects.create(**data)

    else:
        return JsonResponse({'message': 'Algo a une erreur'})

    return JsonResponse({'data': Obf.to_dict()})

### UPDATE
@csrf_exempt
@require_http_methods(['POST'])  
def Obfuscated_update(request, pk):
    obf_up = get_object_or_404(Obfuscated, pk=pk)
    form = ObfuscatedForm(request.POST or None, instance=obf_up)

    if request.POST:
        # Données obtenues par le formulaire.
        if form.is_valid():
            obf_up = form.save()

    elif request.body:
        # Données obtenues via json.
        data = json.loads(request.body)

        for attr, value in data.items():
            setattr(obf_up, attr, value)
        obf_up.save()

    else:
        return JsonResponse({'message': 'Algo a une erreur'})

    return JsonResponse({'data': obf_up.to_dict()})

######### DELETE
@csrf_exempt
@require_http_methods(['DELETE'])
def Obfuscated_delete(request, pk):
    obf_del = get_object_or_404(Obfuscated, pk=pk)
    obf_del.delete()
    return JsonResponse({'data': 'element delete avec succes'})

##########  TEST OBFUSCATED #################
############## GET AND POST LIST
@csrf_exempt
def obfuscateds(request):
    Obfs = Obfuscated.objects.all()
    data = [obf.to_dict() for obf in Obfs]
    form = ObfuscatedForm(request.POST or None)

    if request.method == 'POST':
        if request.POST:
            # Données obtenues par le formulaire.
            if form.is_valid():
                obf = form.save()

        elif request.body:
            # Données obtenues via json.
            data = json.loads(request.body)
            obf = Obfuscated.objects.create(**data)

        else:
            return JsonResponse({'message': 'Algo a une erreur'})

        return JsonResponse({'data': obf.to_dict()})

    return JsonResponse({'data': data})


############## UPDATE, DETAIL AND DELETE OBFUSCATED
@csrf_exempt
def obfuscated(request, pk):
    obf = get_object_or_404(Obfuscated, pk=pk)
    form = ObfuscatedForm(request.POST or None, instance=obf)

    if request.method == 'GET':
        data = obf.to_dict()
        return JsonResponse({'data': data})

    if request.method == 'POST':
        if request.POST:
            # Données obtenues par le formulaire.
            if form.is_valid():
                obf = form.save()

        elif request.body:
            # Données obtenues via json.
            data = json.loads(request.body)

            for attr, value in data.items():
                setattr(obf, attr, value)
            obf.save()

        else:
            return JsonResponse({'message': 'Algo a une erreur'})

        return JsonResponse({'data': obf.to_dict()})

    if request.method == 'DELETE':
        obf.delete()
        return JsonResponse({'data': 'element delete avec succes'})
