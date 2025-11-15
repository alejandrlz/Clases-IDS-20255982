import libros
import estudiantes

#3 Registrar préstamoo

lista_prestamos = []

def registrar_prestamo(lista_libros, lista_estudiantes, lista_prestamos):
    p_carnet = input("Ingrese su carnet: ").upper()

    estudiante_encontrado = False
    estudiante = {}

    for e in estudiantes.lista_estudiantes:
        if p_carnet == e["carnet"]:
            estudiante_encontrado = True
            estudiante = e

    if estudiante_encontrado == False:
        print("Carnet no encontrado")
    else:
        p_codigo = input("Ingrese el código del libro: ").upper()
        
        libro_encontrado = False
        libro = {}

        for l in lista_libros:
            if p_codigo == l["codigo"]:
                libro_encontrado = True
                libro = l

        if libro_encontrado == False:
            print("Código de libro no encontrado")
        else:
            if libro["disponible"] == False:
                print("Libro no disponible")
            else:
                fecha = input("Coloque la fecha: ")
                libro["disponible"] = False

                info_prestamo = {
                    "carnet": p_carnet,
                    "codigo": p_codigo,
                    "fecha": fecha
                }

                lista_prestamos.append(info_prestamo)


#6 Mostar préstamos

def mostrar_prestamos(lista_prestamos):
    if len(lista_prestamos) == 0:
        print("No hay préstamos registrados")
    else:
        for p in lista_prestamos:
            print(f"Carnet: {p['carnet']}")
            print(f"Código del libro: {p['codigo']}")
            print(f"Fecha: {p['fecha']}")
            



