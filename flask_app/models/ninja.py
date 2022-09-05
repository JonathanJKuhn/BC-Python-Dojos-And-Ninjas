from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.fname = db_data['first_name']
        self.lname = db_data['last_name']
        self.age = db_data['age']
        self.dojo = db_data['dojo_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @staticmethod
    def add(data):
        query = "INSERT INTO ninjas (fist_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(age)s, %(dojo)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)