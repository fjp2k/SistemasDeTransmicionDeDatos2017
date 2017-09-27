#empieza aca
from funcion03 import *
conexion=conexionPuerto(puerto,baudrate,timeout)
if(conexion):
    obtenerRespuestas()
else:
    print("No hay conexion")