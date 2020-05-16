"""
Escribir un programa que almacene la cadena de caracateres contraseña en una variable, pregunte
al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario
coincide con la guardada en la variable sin tener en cuenta mayuscula y minusculas
"""

valid_password = "contraseña"

password = input("Introduzca la contraseña: ").lower()

if password == valid_password:
  print("Contraseña correcta. Go on!")
else:
  print("Contraseña incorrecta. Stop!")
