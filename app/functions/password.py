# Funcion de crear contrasena aleatoria.
# La contraseña generada de manera aleatoria contiene numeros, letras y caracteres especiales.
# Se utiliza la funcion shuffle para mezclar los caracteres (barajar).
# Se utiliza la funcion join para concatenar los elementos de la contraseña.
# Se retorna un string de caracteres randomicos.

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


# Funcion de validar contrasena ingresada.
# Se valida que la contraseña contenga un número, una letra y un caracter especial.
# También se valida el tamaño de 8 a 15 caracteres.
# Si se cumplen las cuatro condiciones, se retorna un True, caso contrario un False.
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


