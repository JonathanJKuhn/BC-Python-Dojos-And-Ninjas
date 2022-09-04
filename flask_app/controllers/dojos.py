from flask_app import app
from flask_app.models.dojo import Dojo
from flask import render_template, redirect, request

@app.route('/dojos')
def showDojos():
    return render_template('dojos.html',dojos=Dojo.get_all(),title='Dojos')

@app.route('/dojos/<int:dojoId>')
def showDetails(dojoId):
    return render_template('details.html',title='Dojo Show')

@app.route('/dojos/create', methods=['POST'])
def createDojo():
    data = {
        'name': request.form.get('name')
    }
    Dojo.add(data)
    return redirect('/dojos')