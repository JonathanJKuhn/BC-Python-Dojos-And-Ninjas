from flask_app import app
from flask_app.models.dojo import Dojo
from flask import render_template, redirect, request

@app.route('/dojos')
def showDojos():
    return render_template('dojos.html',dojos=Dojo.get_all(),title='Dojos')

@app.route('/dojos/<int:dojoId>')
def showDetails(dojoId):
    data = { 
        'id': dojoId
        }
    results = Dojo.get_ninjas(data)
    return render_template('details.html',title=f'{results[0].name} Ninjas',dojo=results[0],ninjas=results[1])

@app.route('/dojos/create', methods=['POST'])
def createDojo():
    data = {
        'name': request.form.get('name')
    }
    Dojo.add(data)
    return redirect('/dojos')