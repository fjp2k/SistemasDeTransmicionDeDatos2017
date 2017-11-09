import re


def extraer_datos_por_regex(string, regex):
    try:
        s = string
        trama = re.search(regex, s)

        if trama:
            return trama.group()
        else:
            return None

    except re.error:
        return None
