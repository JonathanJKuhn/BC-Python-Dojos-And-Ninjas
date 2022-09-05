from flask_app import app
from flask import redirect
from flask_app.controllers import dojos
from flask_app.controllers import ninjas

@app.route('/')
def home():
    return redirect('/dojos')

if __name__=="__main__":
    app.run(debug=True)