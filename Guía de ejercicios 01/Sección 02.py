usuario= input("Hola, por favor, ingresa tu nombre: ")
print(f"Bienvenido, {usuario}. Que gusto tenerte aquí")

edad = int(input("Ahora, por favor, ingresa tu edad: "))
print(edad*2)

número1 = int(input("Ahora, ingresa un número: "))
número2 = int(input("Bien ingresa un segundo número: "))
print(f"El resultado es:",número1+número2)

decimal = float(input("Ingresa un número decimal: "))
print(decimal/2)

año_n_usuario= int(input("Ingresa tu año de nacimiento: "))
año_actual = 2025

print(f"Su edad es:{año_actual - año_n_usuario}")

precio = float(input("Ingresa el precio del producto: "))
unidades = int(input("Ingresa cuantas unidades compró: "))

print(f"Total a pagar: ${precio*unidades:.2f}")

n_entero = int(input("Ingresa un número entero: "))

print(f"El cuadrado de ese número es: {n_entero**2}")

n_1 = int(input("Ingresa un número: ")) 
n_2 = int(input("Ingresa otro número: ")) 

print(f"El promedio es: {(n_1+n_2)/2}")

nombre_completo = input("Ingresa tu nombre completo: ")
edad_usuario = input("Escribe tu edad: ")

print(f"Hola, {nombre_completo}. Tienes {edad_usuario}")

