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

    def conectar(self):
        conexionPop.conectar_a_servidor(ssl=False, servidor="localhost",
                                        username="test", contrasenia="123456", frecuencia=0)


    def imprimir(self, mensaje):
        self.gui.info_listbox.delete(0, END)

        self.gui.info_listbox.insert(1,mensaje)

