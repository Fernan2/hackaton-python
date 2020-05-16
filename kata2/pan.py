
precio = 3.49
precio_con_descuento = precio * 0.6
descuento = precio - precio_con_descuento

numero_de_barras = int(input("introduce el número de barras vendidas: "))

print("Precio habitual: " + str(precio))
print("Precio con descuento: " + str(precio_con_descuento))
print("Coste final: " + str(precio_con_descuento * numero_de_barras))
