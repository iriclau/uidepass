# Funcion de crear contrasena aleatoria

import random
import string

letras = string.ascii_letters
numeros = string.digits
caracteres_especiales = string.punctuation


def generar_contrasena_randomica(tamanio: int):
    lista_contrasena = []

    lista_contrasena = lista_contrasena + random.choices(letras, k=int(tamanio / 3))
    lista_contrasena = lista_contrasena + random.choices(numeros, k=int(tamanio / 3))
    lista_contrasena = lista_contrasena + random.choices(caracteres_especiales, k=int(tamanio / 3))

    random.shuffle(lista_contrasena)
    contrasena = "".join(lista_contrasena)
    return contrasena


# Funcion de validar contrasena ingresada

def validar_contrasena_manual(contrasena: str):
    contiene_numero = False
    contiene_letras = False
    contiene_caracter_especial = False
    contiene_tamanio = False
    for elemento in contrasena:

        if elemento in numeros:
            contiene_numero = True
        if elemento in letras:
            contiene_letras = True
        if elemento in caracteres_especiales:
            contiene_caracter_especial = True
    if 8 <= len(contrasena) <= 15:
        contiene_tamanio = True
    return contiene_numero and contiene_letras and contiene_caracter_especial and contiene_tamanio


