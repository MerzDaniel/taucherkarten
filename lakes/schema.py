import graphene

from graphene_django.types import DjangoObjectType
from lakes import models

class CountryType(DjangoObjectType):
    class Meta:
        model = models.Country
class StateType(DjangoObjectType):
    class Meta:
        model = models.State
class DistrictType(DjangoObjectType):
    class Meta:
        model = models.District
class LakeType(DjangoObjectType):
    class Meta:
        model = models.Lake
class DivespotType(DjangoObjectType):
    class Meta:
        model = models.Divespot

class Query(object):
    lakes = graphene.List(LakeType)
    divespots = graphene.List(DivespotType)

    def resolve_lakes(self, info, **kwargs):
        return models.Lake.objects.all()
    def resolve_divespots(self, info, **kwargs):
        return models.Divespot.objects.all()