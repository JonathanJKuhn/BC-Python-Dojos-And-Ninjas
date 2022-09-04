from flask_app import app
from flask_app.controllers import dojos
from flask import redirect, render_template

@app.route('/')
def home():
    return redirect('/dojos')

@app.route('/ninjas')
def ninjas():
    return render_template('add_ninja.html',title='New Ninja')

if __name__=="__main__":
    app.run(debug=True)