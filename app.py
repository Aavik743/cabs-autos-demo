import os
import sys
from flask import Flask, request, Blueprint, json, render_template

from config import PORT
from routes import routes
#from settings import start_process, start_db

"""
Added Project folder path in ROOT_PATH. 
We can use this variable in project to fetch the project folder path.
"""
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
os.environ.update({'ROOT_PATH': ROOT_PATH})
sys.path.append(os.path.join(ROOT_PATH, 'modules'))


"""
flask initialized in app variable
"""
app = Flask(__name__)

"""
Import API blueprints
"""
for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint)



# @app.route("/")
# def index():
#     print("index is running!") 
#     return render_template('home.html')


if __name__ == "__main__":
    app.run(port=PORT, load_dotenv=True, debug=True)  