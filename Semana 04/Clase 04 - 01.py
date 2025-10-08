usuario = "Alejandro" #Tipo String
cantidad_alumnos =79
media_edad = 18.231234
monto_hope = 1234567.890123
inversion_evento = -98765.21548

""""
print(type(cantidad_alumnos))
print(type(media_edad))

print(type(cantidad_alumnos) is int)
print(type(media_edad) is int)"""

# función: un algoritmo con una entrada y salida donde el argumento va entre paréntesis.

"""print("el usuario es",usuario,"y tiene",cantidad_alumnos,"pajaritos en el aula")
print("y la edad promedio es de",media_edad)

print(f"El usuario es {usuario}")
print(f"y en su aula con {cantidad_alumnos - 4} pajaritos")
print(f"con edad promedio de {media_edad:.2f} años") #el ".2f" signficia un punto con 2 decimales fijos
print(f"colectaron ${monto_hope:,.2f} como donativo") #la coma indica que haya separación de miles
print(f"y la totalidad de gastos fue de ${abs(inversion_evento):,.2f} en total")

print(type(usuario) is str)

esta_lloviendo = False

print(type(esta_lloviendo) is not bool)
print(type(monto_hope) is not bool)"""

nombre = "Alejandro"
apellido = "Barrera"

nombre_completo = nombre + " " + apellido #solo se puede concatenar un mismo tipo de dato, en este caso, str
print(nombre_completo)

hola = nombre + " " + str(cantidad_alumnos)
print(hola) #se puede convertir un número a str

