import conexion

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1


class Controlador:

    def __init__(self, gui):

        self.gui = gui

    def configurar_gui(self):

        print "Configurando GUI"

        self.gui.desconectar_btn.config(state=DISABLED)


    def conectar_protocolo_1(self):

        if self.verificar_datos_protocolo_1():
                conexion.conectar_protocolo_1(  equipo=self.gui.idEquipo1.get(),
                                                funcion=self.gui.idCodigoFuncion1.get(),
                                                direccion=self.gui.Entry3.get(),
                                                variables=int(self.gui.Entry4.get())
                                            )

    def conectar_protocolo_2(self):

        if self.verificar_datos_protocolo_2():
                conexion.conectar_protocolo_2(  equipo=self.gui.idEquipo1.get(),
                                    funcion=self.gui.idCodigoFuncion1.get(),
                                    direccion=self.gui.Entry3.get(),
                                    variables=int(self.gui.Entry4.get())
                                )

    def desconectar_protocolo_1(self):
        self.limpiar_pantalla_protocolo_1()

    def desconectar_protocolo_2(self):
        self.limpiar_pantalla_protocolo_2()

    def limpiar_pantalla_protocolo_1(self):
        self.gui.Entry5.delete(0, END)
        self.index_textbox = 0

    def limpiar_pantalla_protocolo_2(self):
        self.gui.tension2.delete(0, END)
        self.index_textbox = 0

    def imprimir_protocolo_1(self, mensaje):
        self.gui.Entry5.insert(self.index_textbox, mensaje)
        self.index_textbox += 1

    def imprimir_protocolo_2(self, mensaje):
        self.gui.tension2.insert(self.index_textbox, mensaje)
        self.index_textbox += 1

    def verificar_datos_protocolo_1(self):

        self.limpiar_pantalla()

        datos_correctos = True

        if self.gui.idEquipo1.get() == '':
            datos_correctos = False
            self.imprimir_protocolo_1("Id equipo vacio")
        elif not self.gui.idEquipo1.get().isdigit():
            datos_correctos = False
            self.imprimir_protocolo_1("El id equipo debe ser un entero positivo")
        elif not isinstance(int(self.gui.idEquipo1.get()), (int, long)):
            datos_correctos = False
            self.imprimir_protocolo_1("El id equipo debe ser un entero positivo")
        elif int(self.gui.idEquipo1.get()) <0 or int(self.gui.idEquipo1.get())>300:
            datos_correctos = False
            self.imprimir_protocolo_1("El id equipo debe debe ser mayor o igual que 0 y menor o igual que 300")



        if self.gui.idCodigoFuncion1.get() == '':
            datos_correctos = False
            self.imprimir_protocolo_1("Id codigo funcion funcion vacio")
        elif not self.gui.idCodigoFuncion1.get().isdigit():
            datos_correctos = False
            self.imprimir_protocolo_1("El id codigo funcion debe ser un entero positivo")
        elif not isinstance(int(self.gui.idCodigoFuncion1.get()), (int, long)):
            datos_correctos = False
            self.imprimir_protocolo_1("El id codigo funcion debe ser un entero positivo")
        elif int(self.gui.idCodigoFuncion1.get()) <0 or int(self.gui.idEquipo1.get())>20:
            datos_correctos = False
            self.imprimir_protocolo_1("El id codigo funcion debe debe ser mayor o igual que 0 y menor o igual que 20")


        if self.gui.Entry3.get() == '':
            datos_correctos = False
            self.imprimir_protocolo_1("Direccion vacio")
        elif not self.gui.Entry3.get().isdigit():
            datos_correctos = False
            self.imprimir_protocolo_1("La direccion debe ser un entero positivo")
        elif not isinstance(int(self.gui.Entry3.get()), (int, long)):
            datos_correctos = False
            self.imprimir_protocolo_1("La direccion debe ser un entero positivo")
        elif int(self.gui.Entry3.get()) <0 or int(self.gui.Entry3.get())>65536:
            datos_correctos = False
            self.imprimir_protocolo_1("La direccion debe debe ser mayor o igual que 0 y menor o igual que 65536")


        if self.gui.Entry4.get() == '':
            datos_correctos = False
            self.imprimir_protocolo_1("Direccion vacio")
        elif not self.gui.Entry4.get().isdigit():
            datos_correctos = False
            self.imprimir_protocolo_1("La cantidad de variables debe ser un entero positivo")
        elif not isinstance(int(self.gui.Entry4.get()), (int, long)):
            datos_correctos = False
            self.imprimir_protocolo_1("La cantidad de variables debe ser un entero positivo")
        elif int(self.gui.Entry4.get()) <0 or int(self.gui.Entry4.get())>500:
            datos_correctos = False
            self.imprimir_protocolo_1("La cantidad de variables debe debe ser mayor o igual que 0 y menor o igual que 500")


        return datos_correctos

    def verificar_datos_protocolo_2(self):

        self.limpiar_pantalla()

        datos_correctos = True

        if self.gui.idEquipo2.get() == '':
            datos_correctos = False
            self.imprimir_protocolo_2("Id equipo vacio")
        elif not self.gui.idEquipo2.get().isdigit():
            datos_correctos = False
            self.imprimir_protocolo_2("El id equipo debe ser un entero positivo")
        elif not isinstance(int(self.gui.idEquipo2.get()), (int, long)):
            datos_correctos = False
            self.imprimir_protocolo_2("El id equipo debe ser un entero positivo")
        elif int(self.gui.idEquipo2.get()) < 0 or int(self.gui.idEquipo2.get()) > 100:
            datos_correctos = False
            self.imprimir_protocolo_2("El id equipo debe debe ser mayor o igual que 0 y menor o igual que 100")

        if self.gui.temperatura.get() == '':
            datos_correctos = False
            self.imprimir_protocolo_2("Temperatura funcion vacio")
        elif not self.gui.temperatura.get().isdigit():
            datos_correctos = False
            self.imprimir_protocolo_2("La temperatura debe ser un entero positivo")
        elif not isinstance(int(self.gui.temperatura.get()), (int, long)):
            datos_correctos = False
            self.imprimir_protocolo_2("La temperatura debe ser un entero positivo")
        elif int(self.gui.temperatura.get()) < 0 or int(self.gui.idEquipo1.get()) > 50:
            datos_correctos = False
            self.imprimir_protocolo_2("El temperatura debe debe ser mayor o igual que 0 y menor o igual que 50")

        if self.gui.corriente.get() == '':
            datos_correctos = False
            self.imprimir_protocolo_2("Corriente vacio")
        elif not self.gui.corriente.get().isdigit():
            datos_correctos = False
            self.imprimir_protocolo_2("La corriente debe ser un entero positivo")
        elif not isinstance(int(self.gui.corriente.get()), (int, long)):
            datos_correctos = False
            self.imprimir_protocolo_2("La corriente debe ser un entero positivo")
        elif int(self.gui.corriente.get()) < 0 or int(self.gui.corriente.get()) > 10:
            datos_correctos = False
            self.imprimir_protocolo_2("La corriente debe debe ser mayor o igual que 0 y menor o igual que 10")

        if self.gui.tension.get() == '':
            datos_correctos = False
            self.imprimir_protocolo_2("Tension vacio")
        elif not self.gui.tension.get().isdigit():
            datos_correctos = False
            self.imprimir_protocolo_2("La tension  debe ser un entero positivo")
        elif not isinstance(int(self.gui.tension.get()), (int, long)):
            datos_correctos = False
            self.imprimir_protocolo_2("La tension debe ser un entero positivo")
        elif int(self.gui.tension.get()) < 0 or int(self.gui.tension.get()) > 220:
            datos_correctos = False
            self.imprimir_protocolo_2("La tension debe debe ser mayor o igual que 0 y menor o igual que 220")

        return datos_correctos