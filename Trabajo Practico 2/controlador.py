import conexionPop

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


class Controlador():

    def __init__(self, gui):
        self.gui = gui

        self.index_textbox = 0

    def configurar_gui(self):
        """
        self.gui.conectar_btn
        self.gui.desconectar_btn
        self.gui.estado_conexion_info


        self.gui.servidor_entry.get()
        self.gui.usuario_entry.get()
        self.gui.contrasenia_entry.get()
        self.gui.frecuencia_entry.get()

        self.gui.puerto_entry.get()
        self.gui.ssl_check.set(0)

        self.gui.info_listbox.delete(0, END)
        """
        print "Configurando GUI"

    def conectar(self):
        conexionPop.conectar_a_servidor(controlador=self,
                                        ssl=False,
                                        servidor="localhost",
                                        username="test",
                                        contrasenia="123456",
                                        frecuencia=5)

    def desconectar(self):
        conexionPop.desconectar()

    def cambiar_mensaje_estado(self, mensaje):
        self.gui.estado_conexion_info.configure(text=''+mensaje+'')

    def limpiar_pantalla(self):
        self.gui.info_listbox.delete(0, END)
        self.index_textbox = 0

    def imprimir(self, mensaje):
        self.gui.info_listbox.insert(self.index_textbox, mensaje)
        self.index_textbox += 1
