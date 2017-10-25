from poplib import *
import threading
import email

# Variables

user = None
frecuencia_recepcion = None


# Funciones

def conectar_a_servidor(ssl, servidor, username, contrasenia, frecuencia, puerto=""):
    thread = threading.Thread(target=ejecutar_conectar_a_servidor(ssl, servidor, puerto, username,
                                                                  contrasenia, frecuencia))
    thread.start()


def ejecutar_conectar_a_servidor(ssl, servidor, puerto, username, contrasenia, frecuencia):
    global user
    global frecuencia_recepcion
    try:
        user = username
        frecuencia_recepcion = frecuencia
        if ssl:
            mailbox = POP3(host=servidor, port=puerto)
        else:
            mailbox = POP3(host=servidor)

        mailbox.user(user)
        mailbox.pass_(contrasenia)

        procesar_emails(mailbox)

    except error_proto as err:
        print "Error: " + err.message

    except Exception as err:
        print "Error: " + err.message


def procesar_emails(mailbox):

    obtener_emails(mailbox=mailbox)


def obtener_emails(mailbox):
    """
    Traer emails del servidor y extrar los mensajes
    :param mailbox:
    :return:
    """
    mensajes_emails = []

    num_messages = len(mailbox.list()[1])
    for i in range(num_messages):
        print 'Mensaje email: ' + str(i)

        if corroborar_remitente():

            for linea_email in mailbox.retr(i + 1)[1]:
                # Se recorre cada linea del email y se obtiene el texto
                cuerpo_email = email.message_from_string(linea_email)

            # Se obtiene el cuerpo del email
            mensaje_email = cuerpo_email.get_payload()
            print mensaje_email
            mensajes_emails.append(mensaje_email)
        else:
            print "Remitente invalido"

    return mensajes_emails

def corroborar_remitente(remitente):
    """
    Se comprueba que el remitente esta en el xml de remitentes habilitados
    :param remitente:
    :return:
    """
    return True

