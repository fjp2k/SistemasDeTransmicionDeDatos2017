import controlador
from Tkinter import *

class Conexion():
    def __init__(self, gui):
        self.gui = gui
        self.id_equipo_1 = 0
        self.id_codigo_funcion_1 = 0
        self.id_direccion_1 = 0
        self.id_cantidad_variables = 0
        self.trama_protocolo = 0
        self.id_temperatura = 0
        self.id_corriente = 0
        self.id_tension = 0



    def conectar_protocolo_1(self,equipo,funcion,direccion,variables):


        self.convertir_datos_protocolo_1(equipo, funcion, direccion, variables)

        id_equipo = self.id_equipo_1[2:self.id_equipo_1.__len__()]
        id_codigo_funcion = self.id_codigo_funcion_1[2:self.id_codigo_funcion_1.__len__()]
        id_direccion = id_direccion_1[2:id_direccion_1.__len__()]
        id_cantidad = id_cantidad_variables[2:id_cantidad_variables.__len__()]
        trama_protocolo = self.id_equipo + self.id_codigo_funcion + self.id_direccion + self.id_cantidad
        print "TRAMA PROTOCOLO 1: %s" % self.trama_protocolo

        self.imprimir_datos_protocolo_1(trama_protocolo)


    def convertir_datos_protocolo_1(equipo,funcion,direccion,variables):
        global id_equipo_1
        global id_codigo_funcion_1
        global id_direccion_1
        global id_cantidad_variables

        id_equipo_1 = bin(equipo)
        id_codigo_funcion_1 = bin(funcion)
        id_direccion_1 = bin(direccion)
        id_cantidad_variables = bin(variables)

    def imprimir_datos_protocolo_1(trama_protocolo):
        controlador.imprimir_protocolo_1(trama_protocolo)

    def desconectar_protocolo_1(self):
        controlador.limpiar_pantalla_protocolo_1()