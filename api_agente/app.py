#problemas con librerias actualizarlas python3 -m pip install --upgrade urllib
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from bson.json_util import dumps
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
import psutil
import platform
import os
   
#acceso y asignacion de variables de entorno
load_dotenv()
database = os.getenv("DATABASE")
user = os.getenv("ADMIN")
pwd = os.getenv("PASSWORD")

#conexion y validacion a la base de datos
try:
    client = MongoClient(f"mongodb+srv://{user}:{pwd}@cluster0.cql9dta.mongodb.net/?retryWrites=true&w=majority",serverSelectionTimeoutMS=200)
    db = client.informacion_detallada    #seleccionar base de datos
    todos = db.prueba #seleccionar colleccion
    info = client.server_info()
    print(info)
except ServerSelectionTimeoutError:
    print(f"bd no conectada, registrar ip ")


#utilizas flask
app = Flask(__name__)

#aceptar todos los origenes de donde puede ser consumida la api
cors = CORS(app, resources={r"/*": {"origins": "*"}})

#endpoint consulta
@app.route("/list", methods=['GET'])
def lists ():
    for x in todos.find({}):
	    return dumps(x), 200

#endpoint agregar
@app.route("/add", methods=['GET'])
def action ():
            
        NameOS = platform.system()
        
        if NameOS == "Darwin":
             #uso de platform y psutil para asignar lo enunciado en el test
            VersionOS = platform.mac_ver()[0]
            UsuariosActivos = psutil.users()[0].name
            InfoProcesador = platform.uname()[3]
            Procesador = platform.processor()
            for proc in psutil.process_iter(['pid', 'name', 'username']):
                todos.insert_one({ "VersionOS":VersionOS,  "UsuariosActivos":UsuariosActivos, "InfoProcesador":InfoProcesador, "Procesador":Procesador,"MaquinaPS":proc.info })
                return dumps({ "insert":NameOS, "UsuariosActivos": UsuariosActivos}), 201
            
        elif NameOS == "Linux":
             #uso de platform y psutil para asignar lo enunciado en el test
            VersionOS = platform.libc_ver()[0]
            UsuariosActivos = psutil.users()[0].name
            InfoProcesador = platform.uname()[3]
            Procesador = platform.processor()
            for proc in psutil.process_iter(['pid', 'name', 'username']):
                todos.insert_one({ "VersionOS":VersionOS,  "UsuariosActivos":UsuariosActivos, "InfoProcesador":InfoProcesador, "Procesador":Procesador,"MaquinaPS":proc.info })
                return dumps({ "insert":NameOS}), 201
            
        elif NameOS == 'Windows':
            #uso de platform y psutil para asignar lo enunciado en el test
            VersionOS = platform.win32_ver()[0]
            UsuariosActivos = psutil.users()[0].name
            InfoProcesador = platform.uname()[3]
            Procesador = platform.processor()
            for proc in psutil.process_iter(['pid', 'name', 'username']):
                todos.insert_one({ "VersionOS":VersionOS,  "UsuariosActivos":UsuariosActivos, "InfoProcesador":InfoProcesador, "Procesador":Procesador,"MaquinaPS":proc.info })
                return dumps({ "insert":NameOS}), 201
        else:
            print('incompatible')

# rutas no encontradas
@app.errorhandler(404)
def page_not_found(error):
    return {"error" : "This page does not exist", "code": 404}, 404

# error conexion
@app.errorhandler(500)
def special_exception_handler(error):
    return {"error" : "Database connection failed", "code": 500}, 500
    
#inicializa el servicio en local y en la ip publica con tls y ssl
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=3000, ssl_context=("./cert/cert.pem", "./cert/key.pem"))