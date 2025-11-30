import modulo_funciones as mf
import modulo_datos as md

#Menú general

activado = True

while activado == True:
    print("--- SISTEMA DE REGISTRO Y PEDIDOS---")
    print("          - CONY COOKIE -")
    
    try:
        opciones_menu = int(input("""1. Registrar cliente
2. Registrar pedido
3. Ver reportes
4. Salir
Elija una opción: """))
    except:
        print("Debe ingresar un número.")
    else:
        if opciones_menu == 1:
            mf.registrar_cliente()
        elif opciones_menu == 2:
            mf.registrar_pedido()
        elif opciones_menu == 3:
            mf.generar_reporte()
        elif opciones_menu == 4:
            mf.salir()
        else:
            print("Debe ingresar una opción válida.")


