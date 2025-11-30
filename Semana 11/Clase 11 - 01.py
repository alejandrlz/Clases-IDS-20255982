def mi_funcion():
    """Esta función imprime un saludo"""
    print("Hola mundo")
    print("Como estás")
    print("Gracias por usarme")

mi_funcion()

def capturar_nombre():
    """Esta función recibe valores por medio de input"""
    nombre_input = input("Escriba su nombre: ")
    apellido_input = input("Digite su apellido: ")
    nombre_completo = f"{nombre_input.capitalize()} {apellido_input.capitalize()}"
    print(nombre_completo)

def capturar_usuario(nombre, edad):
    """Esta funcion recibe valores por medio de argumentos"""
    nombre_usuario = nombre
    edad_usuario = edad
    texto = f"El usuario {nombre_usuario.capitalize()} tiene {edad_usuario} años de edad."
    print(texto)

capturar_usuario("juanito pereZ",74)

def calculo_impuesto(ventas):
    """Esta funcion calcula el valor del impuesto"""
    if ventas < 500:
        tasa_impuesto = 0.1
    else:
        tasa_impuesto = 0.25
    return tasa_impuesto

ventas = 1000
tasa_calculada = calculo_impuesto(ventas)
calculo_total = calculo_impuesto(ventas) *ventas

print(f"""El valor de la venta fue de ${ventas:,.2f},
      la tasa de impuesto es {tasa_calculada},
      y el monto por tanto es ${calculo_total:,.2f}""")