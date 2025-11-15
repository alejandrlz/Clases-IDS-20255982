from codigo import generar_codigo

#1 Registrar libro

lista_libros = []

letra = "L"

def registrar_libro(lista_libros):
    numero = len(lista_libros)
    titulo = input("Inserte el título del libro: ")
    autor = input("Inserte el autor del libro: ")
    codigo = generar_codigo(letra,numero)

    info_libro = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "disponible" : True
    }

    lista_libros.append(info_libro)


#4 Mostrar libros
def mostrar_libros(lista_libros):
    if len(lista_libros) < 1:
        print("No hay libros registrados")
    else:
        for n in lista_libros:
            if n["disponible"] is True:
                estado = "Disponible"
            else:
                estado = "Prestado"

            print(f"Código: {n['codigo']}")
            print(f"Título: {n['titulo']}")
            print(f"Autor: {n['autor']}")
            print(f"Estado: {estado}")


