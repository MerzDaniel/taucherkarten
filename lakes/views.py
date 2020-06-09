from django.shortcuts import render
from django.http import HttpResponse
from lakes import models, queries

# Create your views here.
def index(request):
    lakesByDistrict = queries.getLakesByDistrict()
    
    context = { 'lakesByDistrict': lakesByDistrict }
    return render(request, 'lakes/index.html', context)

def lake(request, lakeSlug):
    lakesByDistrict = queries.getLakesByDistrict()
    lake = models.Lake.objects.get(slug=lakeSlug)
    divespots = models.Divespot.objects.filter(lake=lake)

    context = { 
        'lakesByDistrict': lakesByDistrict, 
        'lake': lake, 
        'divespots': divespots,
        'divespotCount': divespots.count(),
    }
    return render(request, 'lakes/lake.html', context)