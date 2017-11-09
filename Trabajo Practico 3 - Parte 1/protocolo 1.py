id_equipo_1 = 0
id_codigo_funcion_1 = 0
id_direccion_1 = 0
id_cantidad_variables = 0
trama_protocolo_1 = 0

def verificar_id_equipo(id_equipo):
    if(id_equipo >= 0 and id_equipo <= 300):
        global id_equipo_1
        id_equipo_1 = bin(id_equipo)
        print "ID EQUIPO BINARIO: %s" %id_equipo_1
        return True
    else:
        print "Ha ingresado un numero de equipo invalido"
        return False

def verificar_codigo_funcion(id_codigo):
    if(id_codigo>=0 and id_codigo<=20):
        global id_codigo_funcion_1
        id_codigo_funcion_1 = bin(id_codigo)
        print "ID CODIGO FUNCION BINARIO: %s" % id_codigo_funcion_1
        return True
    else:
        print "Ha ingresado un numero de codigo invalido"
        return False

def verificar_direccion(id_direccion):
    if(id_direccion>=0 and id_direccion<=65536):
        global id_direccion_1
        id_direccion_1 = bin(id_direccion)
        print "ID DIRECCION BINARIO: %s" % id_direccion_1
        return True
    else:
        print "Ha ingresado un numero de direccion invalido"
        return False

def verificar_cantidad_variables(id_cantidad):
    if(id_cantidad>=0 and id_cantidad<=500):
        global id_cantidad_variables
        id_cantidad_variables = bin(id_cantidad)
        print "ID CANTIDAD VARAIBLES BINARIO: %s" % id_cantidad_variables
        return True
    else:
        print "Ha ingresado un numero de variables invalido"
        return False

def armar_trama_protocolo():
    global id_equipo_1
    global id_codigo_funcion_1
    global id_direccion_1
    global id_cantidad_variables
    global trama_protocolo_1

    id_equipo = id_equipo_1[2:id_equipo_1.__len__()]
    id_codigo_funcion = id_codigo_funcion_1[2:id_codigo_funcion_1.__len__()]
    id_direccion = id_direccion_1[2:id_direccion_1.__len__()]
    id_cantidad = id_cantidad_variables[2:id_cantidad_variables.__len__()]
    trama = id_equipo + id_codigo_funcion+ id_direccion + id_cantidad
    print "TRAMA PROTOCOLO 1: %s" %trama


if(verificar_id_equipo(12) and verificar_codigo_funcion(20) and verificar_direccion(300) and verificar_cantidad_variables(4)):
    armar_trama_protocolo()
else:
    print "ha ingresado valores incorrectos"

