from django.shortcuts import render
from .models import PetSitter, Pet
from django.db import connection, reset_queries

# decorator
def get_sql_queries(origin_func):
    def wrapper():
        reset_queries()
        origin_func()
        query_info = connection.queries
        for query in query_info:
            print(query['sql'])
    return wrapper

@get_sql_queries
def get_pet_data():
    pets = Pet.objects.all()
    for pet in pets:
        print(f'{pet.name} | 집사 {pet.pet_sitter.first_name}')