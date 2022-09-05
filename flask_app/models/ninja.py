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

    def __repr__(self) -> str:
        return(
            f'id: {self.id}\n'
            f'fname: {self.fname}\n'
            f'lname: {self.lname}\n'
            f'age: {self.age}\n'
            f'dojo: {self.dojo}\n'
            f'created_at: {self.created_at}\n'
            f'updated_at: {self.updated_at}\n'
        )

    @staticmethod
    def add(data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(age)s, %(dojo)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        ninja = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return cls(ninja[0])

    @staticmethod
    def update(data):
        query = "UPDATE ninjas SET first_name = %(fname)s, last_name = %(lname)s, age = %(age)s, dojo_id = %(dojo)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @staticmethod
    def delete(data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)