from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def ninjas():
    dojos = Dojo.get_all()
    return render_template('add_ninja.html',title='New Ninja',dojos=dojos)

@app.route('/ninjas/create', methods=['POST'])
def createNinja():
    data = {
        'dojo': request.form.get('dojo'),
        'fname': request.form.get('fname'),
        'lname': request.form.get('lname'),
        'age': request.form.get('age'),
        'dojo': request.form.get('dojo')
    }
    Ninja.add(data)
    return redirect(f'/dojos/{data["dojo"]}')

@app.route('/ninjas/edit/<int:ninjaId>')
def editNinja(ninjaId):
    data = {
        'id': ninjaId
    }
    ninja_data = Ninja.get(data)
    dojo_data = Dojo.get_all()
    return render_template('edit_ninja.html',title='Edit Ninja',ninja=ninja_data,dojos=dojo_data)

@app.route('/ninjas/update', methods=['POST'])
def updateNinja():
    data = {
        'id': request.form.get('id'),
        'fname': request.form.get('fname'),
        'lname': request.form.get('lname'),
        'age': request.form.get('age'),
        'dojo': request.form.get('dojo')
    }
    Ninja.update(data)
    return redirect(f'/dojos/{data["dojo"]}')

@app.route('/ninjas/delete/<int:ninjaId>/<int:dojoId>')
def deleteNinja(ninjaId, dojoId):
    data = {
        'id': ninjaId
    }
    Ninja.delete(data)
    return redirect(f'/dojos/{dojoId}')