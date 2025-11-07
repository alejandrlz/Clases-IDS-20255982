#1 Configuración inicial
agente = "encargado"
usuario = "" #para permitir que solo sea válido si escribe "encargado"
platillo = []
precios = []
menu = False #para activar y desactivar el menu

#2 Ingreso a la aplicación
while usuario != agente:
    usuario = input("Favor ingrese el nombre del agente: ").lower()
    if usuario == agente:
        menu = True
    else:
        print("Agente no registrado.")

#3 Gestión del menú principal        
while menu is True:
    opcion = int(input("Elija una opción: 1. Creación de platillos, 2. Consulta de platillos y precios, " \
    "3. Colocar un pedido, 4. Salir: "))

#4 Creación de platillos
    if opcion == 1:
         platillo.append(input("Ingrese el nombre del platillo a crear: ").lower())
         precios.append(float(input("Ingrese el precio del platillo a crear: ")))

#5 Consulta de platillos         
    elif opcion == 2:
        if len(platillo) == 0:
             print("Actualmente no hay platillos ingresados")
        else:
            for n in range(len(platillo)):
                print(f"{platillo[n]}: ${precios[n]:.2f}")

#6 Colocar un pedido
    elif opcion == 3:
        n_plato = input("Indique el nombre del platillo para su orden: ").lower()
        if n_plato in platillo:
            i_platillo = platillo.index(n_plato)
            print(f"Usted ha elegido {platillo[i_platillo]} con un precio de ${precios[i_platillo]}")
        else:
            print("El platillo no se encuentra en el menú.")

#7 Salir
    elif opcion == 4:
        menu = False

print("Gracias por usar el sistema.")
    
