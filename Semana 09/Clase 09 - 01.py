"""#Set
my_set = {"rojo", "verde", "negro", "azul", "rojo", "azul"}
#Sirven para obtener una lista de datos que no se repiten
#Por lo que solo toma el "primer" dato que encuentre e ignora a los demás
#es random el orden
print(type(my_set))
print(len(my_set))

print(my_set)

#Diccionario

mascota = {
    "tipo":"perro", 
    "nombre": "Phoenix",
    "edad": 4, 
    "personalidad": "cariñosa"}
# {tipo, nombre, edad, personalidad}
#Pueden tener otros tipos de elementos, son parejas de valores y claves(en lugar de indices
#Clave : valor = item

regys_mascota = {
    "edad" : 4, 
    "nombre" : "Phoeni",
    "personalidad": "cariñosa",
    "tipo" : "perro"}

print(regys_mascota == mascota)"""

birthdays = {
    "Alice": "Apr 1",
    "Bob" : "Dec 12",
    "Carol" : "Mar 4"
}

print(birthdays["Alice"])

print(birthdays)

#items sirve como un indice, pero para los dos, tanto como para la clave como con el valor
#value da solo el valor
#key solo da la clave

for p, d in birthdays.items:
    print(f"El cumpleaños de {p} es el día {d}.")
