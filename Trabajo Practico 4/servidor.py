from flask import Flask, json, request, jsonify

from utils import armar_error, corroborar_datos_trama
from constantes import *

app = Flask(__name__)


@app.route("/getTramas", methods=['GET'])
def obtener_tramas():
    try:
        archivo_parametros = open(DIRECCION_ARCHIVO_TRAMAS, 'r')
        datos = json.load(archivo_parametros)

        tramas = []
        for trama in datos[KEY_TRAMAS]:
            if corroborar_datos_trama(trama):
                tramas.append(trama)

        return jsonify(tramas)
    except IOError:
        return armar_error(error_code=500, error_descripcion='No hay datos')
    except Exception as err:
        return armar_error(error_code=500, error_descripcion=err.message)


@app.route("/getUltimasTramas", methods=["POST"])
def obtener_ultimas_tramas():

    try:
        parametros = request.get_json()

        if KEY_ID_TRAMA not in parametros:
            ultimo_id = 0
        else:
            ultimo_id = parametros[KEY_ID_TRAMA]

        archivo_parametros = open(DIRECCION_ARCHIVO_TRAMAS, 'r')
        datos = json.load(archivo_parametros)

        tramas = []
        if KEY_TRAMAS in datos:
            for trama in datos[KEY_TRAMAS]:
                if corroborar_datos_trama(trama):
                    id_trama = trama[KEY_ID_TRAMA]
                    if id_trama > ultimo_id:
                        tramas.append(trama)

        return jsonify(tramas)

    except IOError:
        return armar_error(error_code=500, error_descripcion='No hay datos')
    except Exception as err:
        if err.message == '':
            return armar_error(error_code=500, error_descripcion=err.description)
        return armar_error(error_code=500, error_descripcion=err.message)
