from codigo import generar_codigo

#2 Registrar estudiante

lista_estudiantes = []
letra = "S"

def registrar_estudiante(lista_estudiante):
    numero = len(lista_estudiantes)
    Nombre = input("Ingrese su nombre: ").title()
    carnet = generar_codigo(letra, numero)

    info_estudiante = {
        "nombre" : Nombre,
        "carnet" : carnet
    }

    lista_estudiantes.append(info_estudiante)

#5 Mostrar estudiantes

def mostrar_estudiantes(lista_estudiante):
    if len(lista_estudiantes) == 0:
        print("No hay estudiantes registrados")
    else:
        for e in lista_estudiantes:
            print(f"Nombre: {e["nombre"]}")
            print(f"Carnet: {e["carnet"]}")
            