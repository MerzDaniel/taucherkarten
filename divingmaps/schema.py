import graphene
import lakes.schema

class Query(lakes.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)