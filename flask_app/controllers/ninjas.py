from flask_app import app
from flask import render_template
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
    dojos = Dojo.get_all()
    return render_template('add_ninja.html',title='New Ninja',dojos=dojos)

@app.route('/ninjas/create', methods=['POST'])
def createNinja():
    pass