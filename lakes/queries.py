
import itertools
from lakes import models

def getLakesByDistrict():
    lakes = models.Lake.objects.select_related('district')
    grouped = itertools.groupby(lakes, key=lambda x: x.district.name)
    lakesByDistrict = [(k, [{'name': l.name, 'slug': l.slug()} for l in lakes]) for k,lakes in grouped]

    return lakesByDistrict