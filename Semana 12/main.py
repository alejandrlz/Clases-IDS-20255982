import modulo_funciones as mf
import modulo_datos as md

def salir():
    print("\nGracias por utilizar el sistema académico. ¡Hasta luego!")
    exit()

def menu_principal():
    while True:
        print("""
=============================
     SISTEMA ACADÉMICO
=============================
1. Registrar estudiante
2. Inscribir en curso
3. Generar reportes
4. Salir
=============================
""")

        try:
            opcion = int(input("Seleccione una opción (1-4): "))
        except:
            print("Ingrese un número válido.")
            continue
        else:
            if opcion == 1:
                mf.registrar_estudiante()
            elif opcion == 2:
                mf.inscribir_en_curso()
            elif opcion == 3:
                mf.generar_reporte()
            elif opcion == 4:
                salir()
            else:
                print("Opción fuera de rango. Intente nuevamente.")

menu_principal()
