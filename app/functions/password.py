import random
import string


letras = string.ascii_letters
numeros = string.digits
caracteres_especiales = string.punctuation


def generar_contrasena_randomica(tamanio: int):
    lista_contrasena = []

    lista_contrasena = lista_contrasena + random.choices(letras, k=int(tamanio/3))
    lista_contrasena = lista_contrasena + random.choices(numeros, k=int(tamanio/3))
    lista_contrasena = lista_contrasena + random.choices(caracteres_especiales, k=int(tamanio/3))

    random.shuffle(lista_contrasena)
    contrasena = "".join(lista_contrasena)
    return contrasena
