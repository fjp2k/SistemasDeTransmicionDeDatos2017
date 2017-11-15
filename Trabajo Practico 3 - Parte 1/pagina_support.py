#! /usr/bin/env python
#
# Support module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Nov 09, 2017 09:53:30 PM


import sys
import controlador 

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


from controlador import Controlador

def conectar_protocolo_1():
    print('pagina_support.conectar_protocolo_1')
    sys.stdout.flush()
    controlador.conectar_protocolo_1()

def conectar_protocolo_2():
    print('pagina_support.conectar_protocolo_2')
    sys.stdout.flush()
    controlador.conectar_protocolo_2

def desconectar_protocolo_1():
    print('pagina_support.desconectar_protocolo_1')
    sys.stdout.flush()
    controlador.desconectar_protocolo_1

def desconectar_protocolo_2():
    print('pagina_support.desconectar_protocolo_2')
    sys.stdout.flush()
    controlador.desconectar_protocolo_2

def init(top, gui, *args, **kwargs):
    global w, top_level, root, controlador
    w = gui
    top_level = top
    root = top

    controlador = Controlador(gui=w)
    controlador.configurar_gui()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import pagina
    pagina.vp_start_gui()


