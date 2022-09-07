from flask import Flask #framework
from dotenv import load_dotenv #variables de entorno
from flask_cors import CORS #cors
from bson.json_util import dumps #formato json
from pymongo import MongoClient #conexion bd
from pymongo.errors import ServerSelectionTimeoutError #errores bd
import psutil #comandos obtener info de la maquina empleados en consola
import platform #arquitectura del equipo
import os #entorno
import getpass
   
#acceso y asignacion de variables de entorno
load_dotenv()
database = os.getenv("DATABASE")
user = os.getenv("ADMIN")
pwd = os.getenv("PASSWORD")

#conexion y validacion a la base de datos
try:
    client = MongoClient(f"mongodb+srv://{user}:{pwd}@cluster0.cql9dta.mongodb.net/?retryWrites=true&w=majority",serverSelectionTimeoutMS=3) #tiempo ejecucion para saber si el servidor algo le paso
    db = client.informacion_detallada    #seleccionar base de datos
    todos = db.prueba #seleccionar colleccion
    info = client.server_info()
    print(info)
except ServerSelectionTimeoutError:
    print(f"bd no conectada, registrar ip ")

#variable global con flask
app = Flask(__name__)

#aceptar todos los origenes de donde puede ser consumida la api
#listas de control acceso /* 
cors = CORS(app, resources={r"/*": {"origins": "*"}})

#endpoint consulta
@app.route("/list", methods=['GET'])
#funcion lists
def lists ():
    listss = []
    for x in todos.find({}).limit(5):
        listss.append(x)
    return dumps(listss), 200

#endpoint agregar
@app.route("/add", methods=['POST', 'GET'])
def add ():
            
        NameOS = platform.system()
        
        if NameOS == "Darwin":
             #uso de platform y psutil para asignar lo enunciado en el test
            VersionOS = platform.mac_ver()[0]
            UsuariosActivos = getpass.getuser()
            InfoProcesador = platform.uname()[3]
            Procesador = platform.processor()
            #declaro array(list) para los procesos
            process = []
            for proc in psutil.process_iter(['pid', 'name', 'username']):
                process.append(proc.info)
                #inserto a la bd mediante funcion insert_one
            todos.insert_one({ "VersionOS":VersionOS,  "UsuariosActivos":UsuariosActivos, "InfoProcesador":InfoProcesador, "Procesador":Procesador,"MaquinaPS":process })
            return dumps({ "proccess":"Insert", "status": 201}), 201
            
        elif NameOS == "Linux":
             #uso de platform y psutil para asignar lo enunciado en el test
            VersionOS = platform.libc_ver()[0]
            UsuariosActivos = getpass.getuser()
            InfoProcesador = platform.uname()[3]
            Procesador = platform.processor()
            process = []
            for proc in psutil.process_iter(['pid', 'name', 'username']):
                process.append(proc.info)
                #inserto a la bd mediante funcion insert_one
            todos.insert_one({ "VersionOS":VersionOS,  "UsuariosActivos":UsuariosActivos, "InfoProcesador":InfoProcesador, "Procesador":Procesador,"MaquinaPS":proc.info })
            return dumps({ "proccess":"Insert", "status": 201}), 201
            
        elif NameOS == 'Windows':
            #uso de platform y psutil para asignar lo enunciado en el test
            VersionOS = platform.win32_ver()[0]
            UsuariosActivos =  getpass.getuser()
            InfoProcesador = platform.uname()[3]
            Procesador = platform.processor()
            process = []
            for proc in psutil.process_iter(['pid', 'name', 'username']):
                process.append(proc.info)
                #inserto a la bd mediante funcion insert_one
            todos.insert_one({ "VersionOS":VersionOS,  "UsuariosActivos":UsuariosActivos, "InfoProcesador":InfoProcesador, "Procesador":Procesador,"MaquinaPS":proc.info })
            return dumps({ "proccess":"Insert", "status": 201}), 201
        else:
            print('incompatible')

# rutas no encontradas
@app.errorhandler(404)
def page_not_found(error):
    return {"error" : "Esta pagina no existe", "code": 404}, 404

# error conexion
@app.errorhandler(500)
def special_exception_handler(error):
    return {"error" : "Error servidor", "code": error}, 500
    
#inicializa el servicio en local y en la ip publica con tls y ssl
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=3000, ssl_context=("./challenge/cert/cert.pem", "./challenge/cert/secret.pem"))
