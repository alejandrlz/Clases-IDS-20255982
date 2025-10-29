"""numeros = ["uno", "dos", "tres", "cuatro"]
print(numeros[0][1])

nombre = "Antonio"
print(nombre.lower().count("a"))"""

#los elementos dentro de una lista son otro conjunto de elementos
#es como ir abriendo carpetas

nombres = ["Ana", "Antonio", "Ana", "Jose",]
"""print(nombres.count("Luis"))
print(nombres[2][1])
#en una lista no puede convertirse a minuscula per se.

r_a = 0
r_a = r_a + nombres[0].lower().count("a")
r_a = r_a + nombres[1].lower().count("a")
r_a = r_a + nombres[2].lower().count("a")
r_a = r_a + nombres[3].lower().count("a")"""

#append e insert sirven para agregar elementoss, append al final e insert según un parámetro
print(nombres)
nombres.append(input("Agregue un nombre al final: "))
print(nombres)
nombres.insert(int(input("Indique el indice: ")),input("Nombre: "))
print(nombres)
nombres.remove("Sebas")
print(nombres)
nombre_borrado = nombres.pop(int(input("Indice a borrar: "))-1)
print(nombres)
print(nombre_borrado)