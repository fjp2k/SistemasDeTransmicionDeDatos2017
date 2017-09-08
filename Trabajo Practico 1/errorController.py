def controlar_trama(trama):

    error_funcion = trama[2:4]

    if error_funcion == '83':
        return False

    elif error_funcion == '86':
       return False

    elif error_funcion == '90':
       return False

    return True


def obtener_error(trama):
    error_funcion = trama[2:4]
    codigo_error = trama[4:6]

    if error_funcion == '83':
        mensaje_error = "Error en funcion 3: " + match_error_code(codigo_error)
        return mensaje_error

    elif error_funcion == '86':
        mensaje_error = "Error en funcion 6: " + match_error_code(codigo_error)
        return mensaje_error

    elif error_funcion == '90':
        mensaje_error = "Error en funcion 16: " + match_error_code(codigo_error)
        return mensaje_error

    return ""

def match_error_code(codigo_error):

    if codigo_error == "01":

        return "ILLEGAL FUNCTION"

    if codigo_error == "02":

        return "ILLEGAL DATA ADDRESS"

    if codigo_error == "03":

        return "ILLEGAL DATA VALUE"

    if codigo_error == "04":

        return "SLAVE DEVICE FAILURE"

    if codigo_error == "05":

        return "ACKNOWLEDGE"

    if codigo_error == "06":

        return "SLAVE DEVICE BUSY"

    if codigo_error == "08":

        return "MEMORY PARITY ERROR"

    if codigo_error == "0A":

        return "GATEWAY PATH UNAVAILABLE"

    if codigo_error == "0B":

        return "GATEWAY TARGET DEVICE FAILED TO RESPOND"

    return "Unknown Error"