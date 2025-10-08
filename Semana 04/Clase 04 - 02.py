cantidad_alumnos = 25
nombre_profe = "Alvin"
nuevas_inscripciones = 0
nombre_profe = input("Ingrese el nombre del profesor: ")
nuevas_inscripciones = int(input("Ahora, ingrese la nueva cantidad de alumnos: "))

print(type(nombre_profe))
print(f"Excelente,",nombre_profe, "es su nuevo profesor.")
print(f"Los alumnos son:",cantidad_alumnos + nuevas_inscripciones)

