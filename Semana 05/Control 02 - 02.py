precios_platos = [3.52, 55.15, 4.25, 60.25, 5.65, 3.15, 2.65, 70.75, 6.25, 2.55]

plato = int(input())
nuevo_precio = float(input())

precios_platos[plato-1] = nuevo_precio

print(f" Los precios actualizados son: {precios_platos}")