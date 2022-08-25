import subprocess
from subprocess import check_output
import json
import requests

sessions = check_output(["who"])
cpuinf = check_output(["who"])
os = check_output(['who'], shell=True)
ver_os = check_output(['who'], shell=True)
process = check_output(['who'], shell=True)
process = check_output(["who"])
date = check_output(["who"])
ip_server = check_output(["who"])


#monitoreo = [cpuinf, process, sessions, os, ver_os ] # lista de array de bits de los comandos ejecutados
nombreArchivo = ver_os.decode("UTF-8") + date.decode("UTF-8") + ".json" # concatenado de nombre de archivo json

monitoring = {
    'commands': {
        'users': sessions.decode("UTF-8"),
        'cpu_info': cpuinf.decode("UTF-8"),
        'operative_system': os.decode("UTF-8"),
        'version_os': ver_os.decode("UTF-8"),
        'process': process.decode("UTF-8")
    }
}


#with open('nombreArchivo.json', 'w') as archivoJson: # open (administra archivos) primer_arg = ruta_archivo segundo_arg = r - read, w-write
    #for dato in monitoring:
        #datoDecodificado = dato.decode() # Decodifica cada array de bits en formato UTF-8 y lo guarda en nueva variable
        #archivoJson.writelines(datoDecodificado)

with open(nombreArchivo, 'w') as file:
    json.dump(monitoring, file, indent=6)

print (monitoring)

 # res --> llevar a formato json
def monitoring_report(nombreArchivo):
    monitoring_report = {'users': sessions, 'cpuinfo': cpuinf,'operative_system': os, 'version_os': ver_os, 'process': process}
    resp = requests.post('172.20.10.3:8080/servers/monitoring', data=monitoring_report)