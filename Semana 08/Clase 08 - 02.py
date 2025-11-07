#Vamos a jugar un juego

"""aprobación= True
while aprobación:
    elección = input("Quieres seguir jugando? (Y/N)")
    if elección[0].lower() == "n":
        aprobación = False
    elif elección[0].lower() == "y":
        print("Me alegra que quieras seguir jugando!")
    else:
        print("La opción elegida no es valida.")"""
    

#Aplicación para registrar alumnos    
"""alumnos = []

for a in range(int(input("Digite la cantidad de alumnos a regitrar: "))):
    alumno = input("Digite el nombre: ")
    alumnos.append(alumno)

print(alumnos)"""

#Sistema de gestión de alumnos

menu_iniciado = True
alumnos = []

while menu_iniciado:
    opción = int(input("1.Agregar, 2.Consultar, 3.Modificar, 4.Borrar, 5.Salir: "))
    if opción == 5:
        menu_iniciado = False
    elif opción == 1:
        alumnos.append(input("Digite el nombre del alumno: "))
    elif opción == 2:
        for a in alumnos:
            print(a)
    elif opción == 3:
        indice = int(input("Digite el numero del alumno (1-3): " ))
        nuevo = input("Digite el nombre nuevo: ")
        alumnos[indice-1] = nuevo
    elif opción == 4:
        indice = int(input("Digite el numero del alumno (1-3) a popear: "))
        alumno_borrado = alumnos.pop(indice-1)
        print(f"Hemos borrado a: {alumno_borrado}")

print("Gracias por usar nuestro sistema :)")        