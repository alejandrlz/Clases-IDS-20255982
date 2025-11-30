import modulo_datos as md
#1 Función registrar cliente
def registrar_cliente():

    cliente_registrado = False

    while cliente_registrado == False:
    
        nombre = input("Ingresa un nombre: ")

        if nombre == "":
            print("No puedes dejar este campo vacío")
        elif len(nombre) < 2:
            print("Tu nombre debe tener mínimo 2 carácteres")
        else:
            cliente_registrado = True

    correo_registrado = False


    while correo_registrado == False:
    
        correo = input("Ingresa un correo: ")

        if correo in md.clientes:
            print("Correo ya registrado con otro cliente.")
        else:
            if correo == "":
                print("No puedes dejar este campo vacío")
            elif correo.count("@") == 0:
                print("Tu correo debe tener un '@'")
            else:
                correo_registrado = True
                print(f"Cliente {nombre} con correo: {correo} registrado correctamente.")
                md.clientes[correo] = nombre
 

#2 Función registrar pedido
def registrar_pedido():
    pedido_registrado = False

    while pedido_registrado == False:
        correo_p = input("Ingrese un correo para su pedido: ").lower()

        if correo_p == "salir":
            pedido_registrado = True

        if correo_p in md.clientes:
            print("---SABORES DISPONIBLES---")

            for c,s in md.sabores.items():
                print(f"{c}: {s}")

            opcion_s_valida = False

            while opcion_s_valida == False:
                opcion_sabor = input("Elija la primera letra del sabor a pedir: ").upper()
                if opcion_sabor.upper() in md.sabores:
                    sabor = md.sabores[opcion_sabor]
                    md.pedidos.append({correo_p: sabor})
                    print("Pedido registrado correctamente.")
                    opcion_s_valida = True
                    pedido_registrado = True
                elif opcion_sabor == "salir":
                    pedido_registrado = True
                else:
                    print("Ingresa una opción de sabor válida.")
        else:
            print("No se encontró el correo ingresado.")
        


#3 Función generar reporte
def generar_reporte():
    if len(md.pedidos) == 0:
        print("No hay pedidos registrados")
        return

    print("""--- OPCIONES DISPONIBLES ---
1. C
2. V
3. F
4. L
5. Clientes sin pedidos
""")

    try:
        opcion = int(input("Elija una opción (1-5): "))
    except:
        print("Opción inválida.")
        return

    if opcion < 1 or opcion > 5:
        print("Opción fuera de rango.")
        return

    if opcion == 5:
        print("--- CLIENTES SIN PEDIDOS ---")
        sin_pedido = []
        for correo in md.clientes:
            tiene = False
            for p in md.pedidos:
                if correo in p:
                    tiene = True
                    break
            if not tiene:
                sin_pedido.append(correo)

        if len(sin_pedido) == 0:
            print("Todos los clientes tienen pedidos.")
        else:
            for c in sin_pedido:
                print(f"- {c}")
        return

    opciones = {1: "C", 2: "V", 3: "F", 4: "L"}
    clave = opciones[opcion]
    sabor = md.sabores[clave]

    print(f"--- CLIENTES QUE PIDIERON {sabor.upper()} ---")

    encontrados = False
    for p in md.pedidos:
        for correo, s in p.items():
            if s == sabor:
                print(f"- {correo}")
                encontrados = True

    if not encontrados:
        print("Nadie pidió este sabor.")




#4 Función salir
def salir():
    print("Gracias por utilizar el sistema. Felices vacaciones :)")
    exit()