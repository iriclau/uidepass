from functions.password import generar_contrasena_randomica,validar_contrasena_manual

contrasena = generar_contrasena_randomica(15)
print(contrasena)
print(validar_contrasena_manual("dhofjffff8*"))