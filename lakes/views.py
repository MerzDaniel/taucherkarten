from django.shortcuts import render
from django.http import HttpResponse
from lakes import models, queries

# Create your views here.
def index(request):
    lakesByDistrict = queries.getLakesByDistrict()
    
    context = { 'lakesByDistrict': lakesByDistrict }
    return render(request, 'lakes/index.html', context)

def lake(request):
    return ''