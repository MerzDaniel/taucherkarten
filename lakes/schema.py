import graphene

from graphene_django.types import DjangoObjectType
from lakes import models

class CountryType(DjangoObjectType):
    class Meta:
        model = models.Country
class StateType(DjangoObjectType):
    class Meta:
        model = models.State
class LakeType(DjangoObjectType):
    class Meta:
        model = models.Lake
class DistrictType(DjangoObjectType):
    class Meta:
        model = models.District
    lakes = graphene.List(LakeType)
    def resolve_lakes(self, info):
        return models.Lake.objects.filter(district_id=self.id)
class DivespotType(DjangoObjectType):
    class Meta:
        model = models.Divespot

class Query(object):
    countries = graphene.List(CountryType)
    states = graphene.List(StateType)
    districts = graphene.List(DistrictType)
    lakes = graphene.List(LakeType)
    divespots = graphene.List(DivespotType)

    def resolve_countries(self, info, **kwargs):
        return models.Country.objects.all()
    def resolve_states(self, info, **kwargs):
        return models.State.objects.all()
    def resolve_districts(self, info, **kwargs):
        return models.District.objects.all()
    def resolve_lakes(self, info, **kwargs):
        return models.Lake.objects.all()
    def resolve_divespots(self, info, **kwargs):
        return models.Divespot.objects.all()