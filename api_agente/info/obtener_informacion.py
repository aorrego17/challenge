from array import array
import psutil
import platform
from .connection import create_connection
## def significa funcion
def Imprimir_resultados(VersionOS,UsuariosActivos,InfoProcesador,Procesador):


    array={}
    array['version']=VersionOS
    array['usuarios']=UsuariosActivos
    array['infoproc']=InfoProcesador
    array['procesador']=Procesador

    clients = create_connection()
    db = clients["pruebas"]
    collection = db["prueba"]
    x = {"name": array}
    collection.insert_one(x)
    return array

def Obtener_info_sistema_operativo():
    NameOS = platform.system()
    if NameOS == "Darwin":
        VersionOS = platform.mac_ver()[0]
        UsuariosActivos = psutil.users()[0].name
        InfoProcesador = platform.uname()[3]
        Procesador = platform.processor()
        MaquinaPS = psutil.pids()
        for procesos in MaquinaPS:
            DetalleProceso = psutil.Process(procesos)
        return Imprimir_resultados(VersionOS,UsuariosActivos,InfoProcesador,Procesador)
    elif NameOS == "Linux":
        VersionOS = platform.libc_ver()[0]
        UsuariosActivos = psutil.users()
        InfoProcesador = platform.uname()[3]
        Procesador = platform.processor()
        MaquinaPS = psutil.pids()
        for procesos in MaquinaPS:
            DetalleProceso = psutil.Process(procesos)
            print(DetalleProceso)  
        return Imprimir_resultados(VersionOS,UsuariosActivos,InfoProcesador,Procesador)
    else:
        VersionOS = platform.win32_ver()[0]
        UsuariosActivos = psutil.users()
        InfoProcesador = platform.uname()[3]
        Procesador = platform.processor()
        MaquinaPS = psutil.pids()
        for procesos in MaquinaPS:
            DetalleProceso = psutil.Process(procesos)
            print(DetalleProceso)
        return Imprimir_resultados(VersionOS,UsuariosActivos,InfoProcesador,Procesador)
        
