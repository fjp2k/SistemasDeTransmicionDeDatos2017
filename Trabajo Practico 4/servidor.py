from flask import Flask, json, request, jsonify
from dateutil import parser

from error_handler import armar_error

app = Flask(__name__)

# Constantes
DIRECCION_ARCHIVO_TRAMAS = 'C:/Users/Facu/Documents/UTN/Sistemas de transmision de datos/Repositorio/' \
                           'Trabajo Practico 3 - Parte 2/tramas.txt'

# Keys
KEY_TRAMAS = "tramas"

KEY_TIMESTAMP = 'timestamp'
KEY_REMITENTE = 'remitente'
KEY_TEMPERATURA = 'temperatura'
KEY_TENSION = 'tension'
KEY_CORRIENTE = 'corriente'
KEY_POTENCIA = 'potencia'
KEY_PRESION = 'presion'


@app.route("/getTramas", methods='GET')
def obtener_tramas():
    try:
        archivo_parametros = open(DIRECCION_ARCHIVO_TRAMAS, 'r')
        datos = json.load(archivo_parametros)
        return jsonify(datos)
    except IOError:
        return armar_error(error_code=500, error_descripcion='No hay datos')
    except Exception as err:
        return armar_error(error_code=500, error_descripcion=err.message)


@app.route("/getUltimasTramas", methods=["POST"])
def obtener_ultimas_tramas():

    try:
        parametros = request.get_json()

        timestamp = parametros[KEY_TIMESTAMP]
        echa_elegida = parser.parse(timestamp)

    

        return jsonify(datos)
    except IOError:
        return armar_error(error_code=500, error_descripcion='No hay datos')
    except Exception as err:
        return armar_error(error_code=500, error_descripcion=err.message)

    if request.method == "POST":
            json_dict = request.get_json()

            stripeAmount = json_dict['stripeAmount']
            stripeCurrency = json_dict['stripeCurrency']
            stripeToken = json_dict['stripeToken']
            stripeDescription = json_dict['stripeDescription']

            data = {'stripeAmountRet': stripeAmount, 'stripeCurrencyRet': stripeCurrency, 'stripeTokenRet': stripeToken,
                    'stripeDescriptionRet': stripeDescription}
            return jsonify(data)
    else:
        return """<html><body>
                Something went horribly wrong
                </body></html>"""