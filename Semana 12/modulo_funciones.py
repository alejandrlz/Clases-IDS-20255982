import modulo_datos as md

def registrar_estudiante():

    registrar = True
    while registrar is True:
        carnet = input("Ingrese un carnet: ")

        try:
            int(carnet)
        except:
            print("Carnet inválido. Solo números.")
        else:
            if len(carnet) >= 6 and len(carnet) <= 10:
                if carnet in md.carnet_estudiantes:
                    print("Carnet ya existente. Ingrese otro.")
                else:
                    md.carnet_estudiantes.append(carnet)
                    registrar = False
            else:
                print("Carnet inválido. Ingréselo nuevamente.")

    registrar = True
    while registrar is True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre) >= 2:
            md.nombre_estudiantes.append(nombre)
            registrar = False
        else:
            print("Nombre debe tener mínimo dos caracteres. Intente nuevamente.")

    registrar = True
    while registrar is True:
        apellido = input("Ingrese su apellido: ")
        if len(apellido) >= 2:
            md.apellido_estudiantes.append(apellido)
            print(f"Usuario con carnet: {carnet} registrado correctamente.")
            registrar = False
        else:
            print("Apellido debe tener mínimo dos caracteres. Intente nuevamente.")


def inscribir_en_curso():

    salir = False
    while salir is False:
        opcion_ins = input("¿Qué deseas hacer? (inscribir o salir): ").lower()

        if opcion_ins == "salir":
            salir = True

        elif opcion_ins == "inscribir":
            carnet_ins_valido = False
            while carnet_ins_valido is False:
                carnet_ins = input("Ingrese un carnet: ")
                if carnet_ins in md.carnet_estudiantes:
                    carnet_ins_valido = True
                else:
                    print("No se encontró el carnet solicitado. Intente nuevamente.")

            print("\n--- LISTA DE CURSOS ---")
            for c, m in md.cursos.items():
                print(f"- {c}: {m}")

            codigo_c_valido = False
            while codigo_c_valido is False:
                codigo_c = input("Ingresa el código de materia para inscribir: ").upper()
                if codigo_c in md.cursos:
                    if (carnet_ins, codigo_c) in md.inscripciones:
                        print("El estudiante ya está inscrito en este curso.")
                    else:
                        codigo_c_valido = True
                else:
                    print("El código de curso ingresado no existe. Intente nuevamente.")

            md.inscripciones.append((carnet_ins, codigo_c))
            print(f"Se inscribió al estudiante con carnet: {carnet_ins} en la materia: {md.cursos[codigo_c]} ({codigo_c}) correctamente ")

        else:
            print("La opción ingresada no es válida. Intente nuevamente.")


def generar_reporte():

    if len(md.inscripciones) == 0:
        print("No hay inscripciones realizadas.")
        return

    print("""--- CURSOS DISPONIBLES ---
1. PY
2. JS
3. BD
4. SE
5. Estudiantes sin inscripción
""")

    try:
        opcion_re = int(input("Elija una opción (1-5): "))
    except:
        print("Opción inválida. Debe ingresar un número.")
        return

    if opcion_re < 1 or opcion_re > 5:
        print("Opción fuera de rango.")
        return

    if opcion_re == 5:
        print("--- ESTUDIANTES SIN INSCRIPCIÓN ---")
        hay_no_inscritos = False

        for c in md.carnet_estudiantes:
            inscrito = False
            for carnet, curso in md.inscripciones:
                if carnet == c:
                    inscrito = True
                    break
            if not inscrito:
                print(f"- {c}")
                hay_no_inscritos = True

        if not hay_no_inscritos:
            print("Todos los estudiantes tienen inscripción.")
        return

    opciones = {
        1: "PY",
        2: "JS",
        3: "BD",
        4: "SE"
    }

    curso_elegido = opciones[opcion_re]

    print(f"--- CARNETS INSCRITOS EN {curso_elegido} ---")

    inscritos = [carnet for carnet, curso in md.inscripciones if curso == curso_elegido]

    if len(inscritos) == 0:
        print("No hay carnets inscritos en este curso.")
    else:
        for carnet in inscritos:
            print(f"- {carnet}")