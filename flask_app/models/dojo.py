from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.ninjas = []

    @staticmethod
    def add(data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @staticmethod
    def get_all():
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        return results

    @classmethod
    def get_ninjas(cls, data):
        dojo_query = "SELECT * FROM dojos WHERE id = %(id)s;"
        dojo = connectToMySQL('dojos_and_ninjas_schema').query_db(dojo_query, data)


        ninjas_query = "SELECT ninjas.id, ninjas.first_name, ninjas.last_name, ninjas.age, ninjas.dojo_id, ninjas.created_at, ninjas.updated_at FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        ninjas = connectToMySQL('dojos_and_ninjas_schema').query_db(ninjas_query, data)
        
        ninja_instances = []

        for ninja in ninjas:
            ninja_instances.append(Ninja(ninja))

        return [cls(dojo[0]), ninja_instances]