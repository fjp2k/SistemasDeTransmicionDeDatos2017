import conexionPop


SERVIDOR = 'localhost'
USERNAME = 'test'
CONTRASENIA = '123456'
FRECUENCIA = 5

SSL = False
PUERTO = ''


def conectar():

    conexionPop.iniciar_conector()

    if SSL:
        conexionPop.conectar_a_servidor(ssl=SSL,
                                        servidor=SERVIDOR,
                                        username=USERNAME,
                                        contrasenia=CONTRASENIA,
                                        frecuencia=FRECUENCIA,
                                        puerto=PUERTO
                                        )
    else:
        conexionPop.conectar_a_servidor(ssl=SSL,
                                        servidor=SERVIDOR,
                                        username=USERNAME,
                                        contrasenia=CONTRASENIA,
                                        frecuencia=FRECUENCIA
                                        )


def desconectar():
    conexionPop.desconectar()

#conectar()
