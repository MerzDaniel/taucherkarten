from django.shortcuts import render
from django.http import HttpResponse
from lakes import models, queries
import itertools

# Create your views here.
def index(request):
    lakesByDistrict = queries.getLakesByDistrict()
    
    context = { 'lakesByDistrict': lakesByDistrict }
    return render(request, 'lakes/index.html', context)

def lake(request, lakeSlug):
    lakesByDistrict = queries.getLakesByDistrict()
    lake = models.Lake.objects.get(slug=lakeSlug)
    divespots = models.Divespot.objects.filter(lake=lake)
    divemapsByDivespot = [(key, [m for m in maps]) \
        for key, maps in itertools.groupby(
        models.Divemap.objects.filter(divespot__in=divespots),
        key=lambda m: m.divespot_id,
    )]

    context = { 
        'lakesByDistrict': lakesByDistrict, 
        'lake': lake, 
        'divespots': divespots,
        'divespotCount': divespots.count(),
        'divemapsByDivespot': divemapsByDivespot,
    }

    return render(request, 'lakes/lake.html', context)

def impressum(request):
    lakesByDistrict = queries.getLakesByDistrict()
    context = { 
        'lakesByDistrict': lakesByDistrict, 
    }
    return render(request, 'lakes/impressum.html', context)

def dataProtection(request):
    lakesByDistrict = queries.getLakesByDistrict()
    context = { 
        'lakesByDistrict': lakesByDistrict, 
    }
    return render(request, 'lakes/data-protection.html', context)