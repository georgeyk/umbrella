from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from schema import schema


app = FastAPI()
app.mount("/gql", GraphQLApp(schema, on_get=make_graphiql_handler()))
