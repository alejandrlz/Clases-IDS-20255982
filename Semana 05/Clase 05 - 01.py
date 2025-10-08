"""nombre = "Alvin" #objeto, cuya etiqueta es "nombre" con un valor de tipo texto
#Un texto es programación es una cadena de caractéres incluyendo los espacios (" ").
palabra= "RECONOCER"
print (nombre[1:4:3]) #inicio:fin:salto / default es -:-:1
print (palabra[-9:])

cantidad = str(123456789)

print(cantidad[2])"""

#ejercicio probando lo que mostraba alvin en clase

print("Creador de contraseñas")

nombre = input("Ingrese su nombre: ")
Año_nacimiento = input("Ingrese su año de nacimiento: ")
Color_favorito= input("Ingrese su color favorito: ")
contraseña_sugerida = Año_nacimiento[:2] + nombre[:3] + Año_nacimiento[2:5] + Color_favorito[::-1]

print(f"Excelente, su contraseña sugerida es: {contraseña_sugerida}")

input("Pulse enter para salir")