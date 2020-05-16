edad = int(input("Introduce tu edad: "))

if edad < 4:
  print("Precio de la entrada: Gratis!")
elif edad <= 18:
  print("Precio de la entrada: 5€")
else:
  print("Precio de la entrada: 10€")
