
#Clientesx|
c_numero = 0
c_letra = "P"
código = c_letra + c_numero

print(código)

nombre = input()
correo = input()
telefono = input()

clientes = {
    "Codigo":código,
    "Nombre": nombre,
    "Correo": correo, 
    "Telefono": telefono}

menu = []

print(clientes)

menu_activado = False

if nombre != "":
    menu_activado = True

while menu_activado == True:
    opciones = print(f"""Bienvenido {nombre}, escoja una ocpión:
1.	Mostrar productos                2.	Agregar producto
3.	Registrar nuevo cliente          4.	Mostrar clientes
5.	Registrar pedido                 6.	Mostrar pedidos del día
7.	Mostrar categorías disponibles   8.	Salir""")
    menu_activado = False

