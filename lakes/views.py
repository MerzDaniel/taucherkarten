from django.shortcuts import render
from django.http import HttpResponse
from lakes import models
import itertools

# Create your views here.
def index(request):
    lakes = models.Lake.objects.select_related('district')
    grouped = itertools.groupby(lakes, key=lambda x: x.district.name)
    lakesByDistrict = [(k, [{'name': l.name, 'slug': l.slug()} for l in lakes]) for k,lakes in grouped]
    
    context = { 'lakesByDistrict': lakesByDistrict }
    return render(request, 'lakes/index.html', context)