import json
import logging
from logging.handlers import RotatingFileHandler

# Direcciones archivos
DIRECCION_ARCHIVO_ERROR_LOGGER = 'C:/Users/Facu/Documents/UTN/Sistemas de transmision de datos/Repositorio/' \
                                 'Trabajo Practico 3 - Parte 2/procesoEmailErrores.log'
DIRECCION_ARCHIVO_INFO_LOGGER = 'C:/Users/Facu/Documents/UTN/Sistemas de transmision de datos/Repositorio/' \
                                'Trabajo Practico 3 - Parte 2/procesoEmailInfo.log'
DIRECCION_ARCHIVO_LOGGER_DINAMICO = 'C:/Users/Facu/Documents/UTN/Sistemas de transmision de datos/Repositorio/' \
                                'Trabajo Practico 3 - Parte 2/procesoEmailDinamico.log'

DIRECCION_ARCHIVO_PARAMETROS_LOGGER_DINAMICO = 'C:/Users/Facu/Documents/UTN/Sistemas de transmision de datos/' \
                                               'Repositorio/Trabajo Practico 3 - Parte 2/parametros_log.json'

# Defaults
DEFAULT_TAMANIO = 5
DEFAULT_CANTIDAD_ARCHIVOS = 3
DEFAULT_NIVEL_LOG = logging.INFO

# Keys parametros
KEY_TAMANIO_ARCHIVO = 'tamanio_kb'
KEY_CANTIDAD_ARCHIVOS = 'cantidad_archivos'
KEY_NIVEL_LOG = 'nivel_log'


class EmailLogger:

    def __init__(self):

        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

        self.error_logger = None
        self.info_logger = None
        self.log_dinamico = None

        self.configurar_log_error(formatter)
        self.configurar_log_info(formatter)
        self.configurar_log_dinamico(formatter)

    def configurar_log_error(self, formatter):
        self.error_logger = logging.getLogger('procesoEmailErrores.log')
        hdlr1 = logging.FileHandler(DIRECCION_ARCHIVO_ERROR_LOGGER)
        hdlr1.setFormatter(formatter)
        self.error_logger.addHandler(hdlr1)
        self.error_logger.setLevel(logging.WARNING)

    def configurar_log_info(self, formatter):
        self.info_logger = logging.getLogger('procesoEmailInfo.log')
        hdlr = logging.FileHandler(DIRECCION_ARCHIVO_INFO_LOGGER)
        hdlr.setFormatter(formatter)
        self.info_logger.addHandler(hdlr)
        self.info_logger.setLevel(logging.INFO)

    def configurar_log_dinamico(self, formatter):

        self.log_dinamico = logging.getLogger('procesoEmailDinamico.log')

        try:
            archivo_parametros = open(DIRECCION_ARCHIVO_PARAMETROS_LOGGER_DINAMICO, 'r')
            parametros = json.load(archivo_parametros)

            tamanio = DEFAULT_TAMANIO
            cantidad_archivos = DEFAULT_CANTIDAD_ARCHIVOS
            nivel_log = DEFAULT_NIVEL_LOG

            if self.chequear_parametros(parametros=parametros):
                tamanio = parametros[KEY_TAMANIO_ARCHIVO]
                cantidad_archivos = parametros[KEY_CANTIDAD_ARCHIVOS]
                nivel_log = self.parsear_nivel_log(parametros[KEY_NIVEL_LOG])

        except IOError:
            tamanio = DEFAULT_TAMANIO
            cantidad_archivos = DEFAULT_CANTIDAD_ARCHIVOS
            nivel_log = DEFAULT_NIVEL_LOG

        hdlr = RotatingFileHandler(
            DIRECCION_ARCHIVO_LOGGER_DINAMICO,
            mode='a',
            maxBytes=tamanio * 1024,
            backupCount=cantidad_archivos,
            encoding=None,
            delay=0
        )
        hdlr.setFormatter(formatter)
        self.log_dinamico.addHandler(hdlr)
        self.log_dinamico.setLevel(nivel_log)

        self.log_dinamico.debug("Nivel log: " + str(nivel_log))
        self.log_dinamico.debug("Tamanio maximo archivo log(kb): " + str(tamanio))
        self.log_dinamico.debug("Cantidad archivos log: " + str(cantidad_archivos))

    def chequear_parametros(self, parametros):

        try:
            tamanio = parametros[KEY_TAMANIO_ARCHIVO]
            cantidad_archivos = parametros[KEY_CANTIDAD_ARCHIVOS]
            nivel_log = parametros[KEY_NIVEL_LOG]

            if not isinstance(tamanio, int):
                return False

            if not isinstance(cantidad_archivos, int):
                return False

            if self.parsear_nivel_log(parametro=nivel_log) == '':
                return False

            return True

        except Exception as err:
            return False

    def parsear_nivel_log(self, parametro):

        if parametro == 'DEBUG':
            return logging.DEBUG

        if parametro == 'INFO':
            return logging.INFO

        elif parametro == 'WARNING':
            return logging.WARNING

        elif parametro == 'ERROR':
            return logging.ERROR

        elif parametro == 'CRITICAL':
            return logging.CRITICAL

        else:
            return ""

    def info(self, msg):
        self.info_logger.info(msg)
        self.error_logger.info(msg)
        self.log_dinamico.info(msg)

    def warning(self, msg):
        self.info_logger.warning(msg)
        self.error_logger.warning(msg)
        self.log_dinamico.warning(msg)

    def error(self, msg):
        self.info_logger.error(msg)
        self.error_logger.error(msg)
        self.log_dinamico.error(msg)

    def critical(self, msg):
        self.info_logger.critical(msg)
        self.error_logger.critical(msg)
        self.log_dinamico.critical(msg)
