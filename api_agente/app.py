from distutils.log import debug
from flask import Flask
from flask_cors import CORS
from resources.router import endpoints

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(endpoints)


if __name__ == '__main__':
    app.run(debug=True)