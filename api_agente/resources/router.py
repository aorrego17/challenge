from flask import request, jsonify, Blueprint
from info import obtener_informacion
from info import connection

endpoints = Blueprint('routes-tasks', __name__)

@endpoints.route('/obtenerinformacion', methods=['GET'])
def info():
    informationSys = obtener_informacion.Obtener_info_sistema_operativo()
    return jsonify(informationSys), 201