import socket
from poplib import *
import threading
import json

import utils
from emailLogger import EmailLogger

# Constantes

DIRECCION_ARCHIVO_TRAMAS = 'C:/Users/Facu/Documents/UTN/Sistemas de transmision de datos/Repositorio/' \
                           'Trabajo Practico 3 - Parte 2/tramas.txt'
DIRECCION_ARCHIVO_REMITENTES = 'C:/Users/Facu/Documents/UTN/Sistemas de transmision de datos/Repositorio/' \
                               'Trabajo Practico 3 - Parte 2/remitentes.txt'


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

KEY_TRAMAS = "tramas"
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

logger = None

user = None
frecuencia_recepcion = None

proceso_analisis_de_emails = None
detener_proceso = None

ultimo_remitente = None


# Funciones
def iniciar_conector():
    global detener_proceso
    global logger

    logger = EmailLogger()

    detener_proceso = threading.Event()


def conectar_a_servidor(ssl, servidor, username, contrasenia, frecuencia, puerto=""):
    global user
    global frecuencia_recepcion
    global proceso_analisis_de_emails
    global detener_proceso

    user = username
    frecuencia_recepcion = frecuencia
    logger.info(msg='Frecuencia proceso: ' + str(frecuencia_recepcion) + ' segundos')

    detener_proceso = threading.Event()
    ejecutar_conectar_a_servidor(ssl, servidor, puerto, contrasenia)


def desconectar():
    if not detener_proceso.is_set():
        logger.info(msg='Desconectando...')
        detener_proceso.set()
    else:
        logger.info(msg='Desconectado')


def ejecutar_conectar_a_servidor(ssl, servidor, puerto, contrasenia):
    logger.info(msg='Conectando a servidor...')
    logger.info(msg='Direccion servidor: ' + str(servidor))
    if puerto != '':
        logger.info(msg='Direccion servidor: ' + str(puerto))
    mailbox = None
    try:

        while not detener_proceso.is_set():
            logger.info(msg='Inicio descarga de emails...')
            if ssl:
                logger.info(msg='Tipo conexion SSL')
                mailbox = POP3(host=servidor, port=puerto)
            else:
                mailbox = POP3(host=servidor)

            logger.info(msg='Usuario: ' + user)
            logger.info(msg='Contrasenia: ' + contrasenia)
            mailbox.user(user)
            mailbox.pass_(contrasenia)

            logger.info(msg='Obteniendo tramas...')
            if procesar_emails(mailbox):
                mailbox.quit()
            logger.info(msg='Obtencion de tramas finalizada')
            logger.info(msg='Sin actividad')
            detener_proceso.wait(frecuencia_recepcion)

        if mailbox:
            # noinspection PyBroadException
            try:
                mailbox.quit()
            except Exception:
                pass
        logger.info(msg='Fin conexion servidor')

    except error_proto as err:
        imprimir_error(err.message)

    except socket.gaierror:
        imprimir_error("La direccion de servidor incorrecta")

    except socket.error:
        imprimir_error("La direccion de servidor incorrecta")

    except Exception as err:
        imprimir_error(err.message)


# noinspection PyBroadException
def procesar_emails(mailbox):
    """
    Traer emails del servidor, extrar los mensajes y procesarlos
    :param mailbox:
    :return:
    """
    try:
        num_messages = len(mailbox.list()[1])
        for numero_mensaje in range(num_messages):
            logger.info(msg='Procesando mensaje email: ' + str(numero_mensaje + 1))

            if corroborar_remitente(numero_mensaje, mailbox):
                trama_email = obtener_trama(numero_mensaje, mailbox)
                if trama_email is not None:
                    diccionario_datos = extraer_datos_trama(trama_email)

                    guardar_datos_trama(diccionario_datos)

                    imprimir_trama(diccionario_datos)

                eliminar_email(mailbox)
            else:
                eliminar_email(mailbox)

        return True

    except error_proto as err:
        imprimir_error(err.message)
        return False

    except Exception as err:
        imprimir_error(err.message)
        return False


def corroborar_remitente(numero_mensaje, mensajes):
    """
    Se comprueba que el remitente esta en el json de remitentes habilitados
    :param numero_mensaje:
    :param mensajes:
    :return: devuelve verdadero si esta el remitente esta en el json
    """
    global ultimo_remitente
    datos = ""
    for linea_email in mensajes.retr(numero_mensaje + 1)[1]:
        if linea_email[0:4] == 'From':
            remitente = utils.extraer_datos_por_regex(linea_email, REGEX_EMAIL)
            if remitente is not None:
                datos = remitente
            break

    logger.info("Comprobando remitente: " + datos)
    with open(DIRECCION_ARCHIVO_REMITENTES) as json_file:
        data = json.load(json_file)
        for usuario in data[KEY_REMITENTES]:
            if usuario[KEY_REMITENTE] == datos:
                logger.info(msg="Remitente valido")
                ultimo_remitente = datos
                return True
        logger.warning(msg="Remitente invalido")
        ultimo_remitente = None
        return False


def obtener_trama(numero_mensaje, mensajes):
    logger.info(msg='Obteniendo trama')
    for linea_email in mensajes.retr(numero_mensaje + 1)[1]:
        # Se recorre cada linea del email y se comprueba si es una trama
        trama = utils.extraer_datos_por_regex(linea_email, REGEX_TRAMA)
        if trama is not None:
            logger.info('Trama: ' + trama)
            return trama
    logger.warning(msg='Remitente: ' + ultimo_remitente + ' - No se encontro trama en el email o es incorrecta')
    return None


def eliminar_email(mailbox):
    try:
        logger.info(msg='eliminando email: ' + mailbox.list()[1][0].split(' ')[0])
        mailbox.dele(int(mailbox.list()[1][0].split(' ')[0]))
    except error_proto as err:
        imprimir_error('Error eliminando mensaje: ' + err.message)
        pass


def extraer_datos_trama(trama_email):
    logger.info(msg='Extrayendo datos trama: ' + trama_email)
    timestamp_trama = utils.extraer_datos_por_regex(trama_email, REGEX_TRAMA_TIMESTAMP)
    timestamp = timestamp_trama[1:-1]

    datos_trama = utils.extraer_datos_por_regex(trama_email, REGEX_TRAMA_DATOS)
    datos = datos_trama[1:-1]
    datos_array = datos.split(',')

    if datos_array.__len__() == 5:

        remitente = 'Remitente desconocido'
        if ultimo_remitente:
            remitente = ultimo_remitente

        diccionario_datos = {
            KEY_TIMESTAMP: timestamp,
            KEY_REMITENTE: remitente,
            KEY_TEMPERATURA: datos_array[0].strip(),
            KEY_TENSION: datos_array[1].strip(), KEY_CORRIENTE: datos_array[2].strip(),
            KEY_POTENCIA: datos_array[3].strip(), KEY_PRESION: datos_array[4].strip()
        }
        return diccionario_datos

    else:
        logger.info('Datos vacios')
        return None


def guardar_datos_trama(diccionario_trama):
    """
    Guardar los datos de una trama en el json
    :param diccionario_trama:
    :return:
    """
    try:
        logger.info(msg='Abriendo archivo tramas')
        file_tramas = open(DIRECCION_ARCHIVO_TRAMAS, 'r')
    except IOError:
        logger.warning(msg='Error abriendo archivo tramas')
        logger.info(msg='Creando nuevo archivo de tramas')
        file_tramas = open(DIRECCION_ARCHIVO_TRAMAS, 'w')
        file_tramas.write('{"tramas":[]}')
        file_tramas = open(DIRECCION_ARCHIVO_TRAMAS, 'r')

    with file_tramas as json_file:
        data = json.load(json_file)
        data[KEY_TRAMAS].append(diccionario_trama)
        with open(DIRECCION_ARCHIVO_TRAMAS, 'w') as json_file_w:
            logger.info(msg='Guardando trama')
            json.dump(data, json_file_w)


def imprimir_trama(diccionario_datos):
    """
    A partir del diccionario de una trama, imprimir por pantalla los resultados
    :param diccionario_datos:
    :return:
    """

    timestamp = diccionario_datos[KEY_TIMESTAMP]
    remitente = diccionario_datos[KEY_REMITENTE]
    temperatura = diccionario_datos[KEY_TEMPERATURA]
    tension = diccionario_datos[KEY_TENSION]
    corriente = diccionario_datos[KEY_CORRIENTE]
    potencia = diccionario_datos[KEY_POTENCIA]
    presion = diccionario_datos[KEY_PRESION]

    string_a_imprimir = 'Timestamp: ' + timestamp + ' ' + remitente + '-> Temperatura: ' + \
                        str(temperatura) + ' / Tension: ' + str(tension) + ' / Corriente: ' \
                        + str(corriente) + ' / Potencia: ' + str(potencia) + ' / Presion: ' \
                        + str(presion)

    logger.info(msg='Nueva trama: ' + string_a_imprimir)


def imprimir_error(mensaje):
    if not detener_proceso.is_set():
        logger.error(msg='Error de conexion')
        logger.error(msg=mensaje)
        detener_proceso.set()
    else:
        logger.error(msg='Error de conexion')
        logger.error(msg='Desconectado')
