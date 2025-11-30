def registro_profesores(nombre, apellidos, **materias):
    """Crear un registro de profesor, usando kwargs"""
    print(f"El profesor {nombre} {apellidos} imparte las materias:")
    for ciclo, materias in materias.items():
        print(f"    - {ciclo}:  {materias}")


def ordenar_pizza(size, masa, *ingredientes): #ahora con args
    """Vamos a imprimir su orden"""
    print(f"Usted ha ordenado una pizza {size} de {masa} con:")
    for i in ingredientes:
        print(f"- {i.capitalize()}")

def saludar_usuarios(nombres):
    """Saludará usuario"""
    for n in nombres:
        print(f"Hola, {n.capitalize()}")


