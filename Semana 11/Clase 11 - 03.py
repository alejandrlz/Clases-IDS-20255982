def registro_profesores(nombre, apellidos, **materias):
    """Crear un registro de profesor, usando kwargs"""
    print(f"El profesor {nombre} {apellidos} imparte las materias:")
    for ciclo, materias in materias.items():
        print(f"    - {ciclo}:  {materias}")

registro_profesores(
    "pEpe",
    "hernandez", 
    ciclo1 = ["ciencias", "lenguaje", "mate"],
    ciclo2 = ["algebra", "diseño", "arte"])