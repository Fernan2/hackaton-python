valid_password = "contraseña"

password = input("Introduzca la contraseña: ").lower()

if password == valid_password:
  print("Contraseña correcta. Go on!")
else:
  print("Contraseña incorrecta. Stop!")
