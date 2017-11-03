from poplib import *
import threading
import email
import re
import json


# Constantes
KEY_MENSAJES = 'mensajes'
KEY_EMAIL = 'email'
KEY_TIMESTAMP = 'timestamp'
KEY_REMITENTES = 'remitentes'
KEY_TEMPERATURA = 'temperatura'
KEY_TENSION = 'tension'
KEY_CORRIENTE = 'corriente'
KEY_POTENCIA = 'potencia'
KEY_PRESION = 'presion'
KEY_REMITENTE = 'remitente'

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
        controlador_gui.cambiar_mensaje_estado('Conectando: obteniendo tramas')

        while not detener_proceso.is_set():
            procesar_emails(mailbox)
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

        if corroborar_remitente(""):

            trama_email = obtener_trama(numero_mensaje, mailbox)
            if trama_email is not None:
                diccionario_datos = extraer_datos_trama(trama_email)
                mensajes_emails.append(mensaje_email)
        else:
            print "Remitente invalido"

    return mensajes_emails


def corroborar_remitente(remitente):
    """
    Se comprueba que el remitente esta en el json de remitentes habilitados
    :param remitente:
    :return: devuelve verdadero si esta el remitente esta en el json
    """
    with open('remitentes.txt') as json_file:
        data = json.load(json_file)
        print data
        for usuario in  data[KEY_REMITENTES]:
            if usuario[KEY_REMITENTE] == remitente:
                return True
        return False



def obtener_trama(numero_mensaje, mensajes):
    for linea_email in mensajes.retr(numero_mensaje + 1)[1]:
        # Se recorre cada linea del email y se comprueba si es una trama
        trama = corroborar_trama(linea_email)
        if trama is not None:
            return trama
    return None


def corroborar_trama(mensaje_email):
    try:
        s = mensaje_email
        trama = re.search('>.+?<', s)

        if trama:
            return trama.group()
        else:
            return None

    except Exception as err:
        return None

def extraer_datos_trama(trama_email):






def guardar_datos_trama(diccionario_trama):
    """
    Guardar los datos de una trama en el json
    :param trama:
    :return:
    """
    with open('mensajes.txt') as json_file:
        data = json.load(json_file)
        data[KEY_MENSAJES].append(diccionario_trama)
        with open('mensajes.txt', 'w') as json_file:
            json.dump(data,json_file)
    # TODO


def imprimir_trama(diccionario_datos):
    """
    A partir del diccionario de una trama, imprimir por pantalla los resultados
    :param diccionario_datos:
    :return:
    """
    # TODO

    timestamp = ''
    temperatura = ''
    tension = ''
    corriente = ''
    potencia = ''
    presion = ''
    timestamp = diccionario_datos[KEY_TIMESTAMP]
    temperatura = diccionario_datos[KEY_TEMPERATURA]
    tension = diccionario_datos[KEY_TENSION]
    corriente = diccionario_datos[KEY_CORRIENTE]
    potencia = diccionario_datos[KEY_POTENCIA]
    presion = diccionario_datos[KEY_PRESION]

    string_a_imprimir = 'Timestamp: ' + timestamp + ' -> Temperatura: ' + temperatura \
                        + ' / Tension: ' + tension +  ' / Corriente: ' + corriente \
                        + ' / Potencia: ' + potencia + ' / Presion: ' + presion

    controlador_gui.imprimir(string_a_imprimir)