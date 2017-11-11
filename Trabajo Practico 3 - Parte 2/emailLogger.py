import logging

DIRECCION_ARCHIVO_ERROR_LOGGER = 'C:/Users/Facu/Documents/UTN/Sistemas de transmision de datos/Repositorio/' \
                                 'Trabajo Practico 3 - Parte 2/procesoEmailErrores.log'
DIRECCION_ARCHIVO_INFO_LOGGER = 'C:/Users/Facu/Documents/UTN/Sistemas de transmision de datos/Repositorio/' \
                                'Trabajo Practico 3 - Parte 2/procesoEmailInfo.log'


class EmailLogger:

    def __init__(self):

        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

        self.error_logger = logging.getLogger('procesoEmailErrores.log')
        hdlr1 = logging.FileHandler(DIRECCION_ARCHIVO_ERROR_LOGGER)
        hdlr1.setFormatter(formatter)
        self.error_logger.addHandler(hdlr1)
        self.error_logger.setLevel(logging.WARNING)

        self.info_logger = logging.getLogger('procesoEmailInfo.log')
        hdlr2 = logging.FileHandler(DIRECCION_ARCHIVO_INFO_LOGGER)
        hdlr2.setFormatter(formatter)
        self.info_logger.addHandler(hdlr2)
        self.info_logger.setLevel(logging.INFO)

    def info(self, msg):
        self.info_logger.info(msg)
        self.error_logger.info(msg)

    def warning(self, msg):
        self.info_logger.warning(msg)
        self.error_logger.warning(msg)

    def error(self, msg):
        self.info_logger.error(msg)
        self.error_logger.error(msg)

    def critical(self, msg):
        self.info_logger.critical(msg)
        self.error_logger.critical(msg)
