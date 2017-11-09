id_equipo_1 = 0
id_temperatura = 0
id_corriente = 0
id_tension = 0
trama_protocolo_1 = 0

def verificar_id_equipo(id_equipo):
    if(id_equipo >= 0 and id_equipo <= 100):
        global id_equipo_1
        id_equipo_1 = bin(id_equipo)
        print "ID EQUIPO BINARIO: %s" %id_equipo_1
        return True
    else:
        print "Ha ingresado un numero de equipo invalido"
        return False

def verificar_temperatura(temperatura):
    if(temperatura>=0 and temperatura<=50):
        global id_temperatura
        id_temperatura = bin(temperatura)
        print "ID TEMPERATURA BINARIO: %s" % id_temperatura
        return True
    else:
        print "Ha ingresado un numero de temperatura invalido"
        return False

def verificar_corriente(corriente):
    if(corriente>=0 and corriente<=10):
        global id_corriente
        id_corriente = bin(corriente)
        print "ID CORRIENTE BINARIO: %s" % id_corriente
        return True
    else:
        print "Ha ingresado un numero de corriente invalido"
        return False

def verificar_tension(tension):
    if(tension>=0 and tension<=220):
        global id_tension
        id_tension = bin(tension)
        print "ID TENSION BINARIO: %s" % id_tension
        return True
    else:
        print "Ha ingresado un numero de tension invalido"
        return False

def armar_trama_protocolo():
    global id_equipo_1
    global id_temperatura
    global id_corriente
    global id_tension
    global trama_protocolo_1

    id_equipo = id_equipo_1[2:id_equipo_1.__len__()]

    temperatura = id_temperatura[2:id_temperatura.__len__()]

    corriente = id_corriente[2:id_corriente.__len__()]

    tension = id_tension[2:id_tension.__len__()]

    trama = id_equipo + temperatura+ corriente + tension
    print "TRAMA PROTOCOLO 1: %s" %trama


if(verificar_id_equipo(12) and verificar_temperatura(20) and verificar_corriente(10) and verificar_tension(4)):
    armar_trama_protocolo()
else:
    print "ha ingresado valores incorrectos"