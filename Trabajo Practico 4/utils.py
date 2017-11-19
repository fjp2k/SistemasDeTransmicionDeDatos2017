from flask import jsonify
from constantes import *


def armar_error(error_code, error_descripcion):
    content = {KEY_ERROR_DESCRIPTION: error_descripcion, KEY_ERROR_CODE: error_code}
    return jsonify(content)


def corroborar_datos_trama(trama):
    if KEY_ID_TRAMA not in trama:
        return False
    if not isinstance(trama[KEY_ID_TRAMA], int):
        return False

    if KEY_TIMESTAMP not in trama:
        return False

    if KEY_REMITENTE not in trama:
        return False

    if KEY_TEMPERATURA not in trama:
        return False

    if KEY_TENSION not in trama:
        return False

    if KEY_CORRIENTE not in trama:
        return False

    if KEY_POTENCIA not in trama:
        return False

    if KEY_PRESION not in trama:
        return False

    return True
