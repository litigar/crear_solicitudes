import re


def solo_numeros(phrase):
    # Quita los caracteres especiales de las cadenas
    # print(f"quitarCaracteresEspeciales phrase {phrase}")
    allow = '0123456789'
    # print(f"quitarCaracteresEspeciales allow {allow}")
    cadena = re.sub('[^%s]' % allow, '', phrase)
    # print(cadena)
    # print(f"quitarCaracteresEspeciales cadena {cadena}")
    return cadena
