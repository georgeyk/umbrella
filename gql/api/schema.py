import graphene

from masoniteorm.query import QueryBuilder


class UserType(graphene.ObjectType):
    id = graphene.UUID()
    name = graphene.String()
    username = graphene.String()
    email = graphene.String()


class Query(graphene.ObjectType):
    user = graphene.Field(UserType)
    users = graphene.Field(graphene.List(UserType), limit=graphene.Int())

    def resolve_user(root, info):
        pass

    def resolve_users(root, info, limit):
        builder = QueryBuilder().table("users")
        limit = limit if limit and limit < 100 else 100
        return builder.limit(limit).all()


schema = graphene.Schema(query=Query)
