from poplib import *
import threading

# Variables

user = None
frecuencia_recepcion = None


# Funciones

def conectar_a_servidor(ssl, servidor, username, contrasenia, frecuencia, puerto=""):
    thread = threading.Thread(target=ejecutar_conectar_a_servidor(ssl, servidor, puerto, username, contrasenia, frecuencia))
    thread.start()

def ejecutar_conectar_a_servidor(ssl, servidor, puerto, username, contrasenia, frecuencia):
    global user
    global frecuencia_recepcion
    try:
        user = username
        frecuencia_recepcion = frecuencia
        mailbox = None
        if ssl:
            mailbox = POP3(host=servidor, port=puerto)
        else:
            mailbox = POP3(host=servidor)

        mailbox.user(user)
        mailbox.pass_(contrasenia)

        obtener_mails(mailbox=mailbox)


    except error_proto as err:
        print "Error: " + err.message

    except Exception as err:
        print "Error: " + err.message


def obtener_mails(mailbox):
    num_messages = len(mailbox.list()[1])
    for i in range(num_messages):
        (server_msg, body, octets) = mailbox.retr(i)
        print (body)