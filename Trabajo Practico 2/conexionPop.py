from poplib import *
import threading
import json

import utils


# Constantes

REGEX_TIMESTAMP = '[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])T(2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9]'
REGEX_DATOS = '[ \t]*[+-]?([0-9]*[.])?[0-9]+[ \t]*,' \
              '[ \t]*[+-]?([0-9]*[.])?[0-9]+[ \t]*,' \
              '[ \t]*[+-]?([0-9]*[.])?[0-9]+[ \t]*,' \
              '[ \t]*[+-]?([0-9]*[.])?[0-9]+[ \t]*,' \
              '[ \t]*[+-]?([0-9]*[.])?[0-9]+[ \t]*'

REGEX_TRAMA = '>' + REGEX_TIMESTAMP + ';' + REGEX_DATOS + '<'
REGEX_TRAMA_TIMESTAMP = '>' + REGEX_TIMESTAMP + ';'
REGEX_TRAMA_DATOS = ';' + REGEX_DATOS + '<'

REGEX_EMAIL = '[\b]*[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[\b]*'

KEY_MENSAJES = 'mensajes'
KEY_EMAIL = 'email'
KEY_REMITENTES = 'remitentes'
KEY_REMITENTE = 'remitente'

KEY_TIMESTAMP = 'timestamp'
KEY_TEMPERATURA = 'temperatura'
KEY_TENSION = 'tension'
KEY_CORRIENTE = 'corriente'
KEY_POTENCIA = 'potencia'
KEY_PRESION = 'presion'

# Variables

controlador_gui = None
user = None
frecuencia_recepcion = None

proceso_analisis_de_emails = None
detener_proceso = None


# Funciones

def conectar_a_servidor(controlador, ssl, servidor, username, contrasenia, frecuencia, puerto=""):
    global controlador_gui
    global user
    global frecuencia_recepcion
    global proceso_analisis_de_emails
    global detener_proceso

    controlador_gui = controlador
    user = username
    frecuencia_recepcion = frecuencia

    # inicio hilo que trae los emails y los procesa
    detener_proceso = threading.Event()
    proceso_analisis_de_emails = threading.Thread(target=ejecutar_conectar_a_servidor,
                                                  args=(ssl, servidor, puerto, contrasenia,))
    proceso_analisis_de_emails.start()


def desconectar():
    controlador_gui.cambiar_mensaje_estado('Desconectando...')
    detener_proceso.set()


def ejecutar_conectar_a_servidor(ssl, servidor, puerto, contrasenia):
    controlador_gui.cambiar_mensaje_estado('Conectando a servidor')
    try:

        obtener_datos_almacenados()

        if ssl:
            mailbox = POP3(host=servidor, port=puerto)
        else:
            mailbox = POP3(host=servidor)

        mailbox.user(user)
        mailbox.pass_(contrasenia)

        while not detener_proceso.is_set():
            controlador_gui.cambiar_mensaje_estado('Conectado: obteniendo tramas')
            procesar_emails(mailbox)

            controlador_gui.cambiar_mensaje_estado('Conectando: sin actividad')
            detener_proceso.wait(frecuencia_recepcion)

        controlador_gui.cambiar_mensaje_estado('Desconectando...')

    except error_proto as err:
        controlador_gui.cambiar_mensaje_estado('Error en conexion: '+err.message)
        print "Error: " + err.message

    except Exception as err:
        controlador_gui.cambiar_mensaje_estado('Error en conexion: ' + err.message)
        print "Error: " + err.message


def obtener_datos_almacenados():
    """
    Buscar las tramas leidas con anterioridad y mostrarlas por pantalla
    :return:
    """
    controlador_gui.limpiar_pantalla()

    datos_almacenados = leer_datos_bd()

    for trama in datos_almacenados[KEY_MENSAJES]:
        imprimir_trama(trama)


def leer_datos_bd():
    """
    Devolver lista con cada una de las tramas almacenadas
    :return:
    """
    with open('mensajes.txt') as json_file:
        data = json.load(json_file)
        return data


def procesar_emails(mailbox):
    """
    Traer emails del servidor, extrar los mensajes y procesarlos
    :param mailbox:
    :return:
    """
    mensajes_emails = []

    num_messages = len(mailbox.list()[1])
    for numero_mensaje in range(num_messages):
        print 'Mensaje email: ' + str(numero_mensaje)

        if corroborar_remitente(numero_mensaje, mailbox):

            trama_email = obtener_trama(numero_mensaje, mailbox)
            if trama_email is not None:
                diccionario_datos = extraer_datos_trama(trama_email)

                guardar_datos_trama(diccionario_datos)

                imprimir_trama(diccionario_datos)

                eliminar_email(numero_mensaje, mailbox)
                mensajes_emails.append(trama_email)
        else:
            mailbox.dele(numero_mensaje)
            print "Remitente invalido"

    return mensajes_emails


def corroborar_remitente(numero_mensaje, mensajes):
    """
    Se comprueba que el remitente esta en el json de remitentes habilitados
    :param numero_mensaje:
    :param mensajes:
    :return: devuelve verdadero si esta el remitente esta en el json
    """
    datos = ""
    for linea_email in mensajes.retr(numero_mensaje + 1)[1]:
        if linea_email[0:4] == 'From':
            remitente = utils.extraer_datos_por_regex(linea_email, REGEX_EMAIL)
            if remitente is not None:
                datos = remitente
            break

    with open('remitentes.txt') as json_file:
        data = json.load(json_file)
        print data
        for usuario in data[KEY_REMITENTES]:
            if usuario[KEY_REMITENTE] == datos:
                return True
        return False


def obtener_trama(numero_mensaje, mensajes):
    for linea_email in mensajes.retr(numero_mensaje + 1)[1]:
        # Se recorre cada linea del email y se comprueba si es una trama
        trama = utils.extraer_datos_por_regex(linea_email, REGEX_TRAMA)
        if trama is not None:
            return trama
    return None


def eliminar_email(numero_email, mailbox):
    try:
        mailbox.dele(int(mailbox.list()[1][numero_email].split(' ')[0]))
    except error_proto as err:
        print "Error liminando mensaje"
        pass

def extraer_datos_trama(trama_email):

    timestamp_trama = utils.extraer_datos_por_regex(trama_email, REGEX_TRAMA_TIMESTAMP)
    timestamp = timestamp_trama[1:-1]

    datos_trama = utils.extraer_datos_por_regex(trama_email, REGEX_TRAMA_DATOS)
    datos = datos_trama[1:-1]
    datos_array = datos.split(',')

    if datos_array.__len__() == 5:

        diccionario_datos = {
            KEY_TIMESTAMP: timestamp,
            KEY_TEMPERATURA: datos_array[0].strip(),
            KEY_TENSION: datos_array[1].strip(), KEY_CORRIENTE: datos_array[2].strip(),
            KEY_POTENCIA: datos_array[3].strip(), KEY_PRESION: datos_array[4].strip()
        }
        return diccionario_datos

    else:
        return None


def guardar_datos_trama(diccionario_trama):
    """
    Guardar los datos de una trama en el json
    :param diccionario_trama:
    :return:
    """
    with open('mensajes.txt') as json_file:
        data = json.load(json_file)
        data[KEY_MENSAJES].append(diccionario_trama)
        with open('mensajes.txt', 'w') as json_file_w:
            json.dump(data, json_file_w)


def imprimir_trama(diccionario_datos):
    """
    A partir del diccionario de una trama, imprimir por pantalla los resultados
    :param diccionario_datos:
    :return:
    """

    timestamp = diccionario_datos[KEY_TIMESTAMP]
    temperatura = diccionario_datos[KEY_TEMPERATURA]
    tension = diccionario_datos[KEY_TENSION]
    corriente = diccionario_datos[KEY_CORRIENTE]
    potencia = diccionario_datos[KEY_POTENCIA]
    presion = diccionario_datos[KEY_PRESION]

    string_a_imprimir = 'Timestamp: ' + timestamp + ' -> Temperatura: ' + temperatura \
                        + ' / Tension: ' + tension + ' / Corriente: ' + corriente \
                        + ' / Potencia: ' + potencia + ' / Presion: ' + presion

    controlador_gui.imprimir(string_a_imprimir)
