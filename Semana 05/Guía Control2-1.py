#1) Capturar artículos producidos
"""c_enero = 1.25
c_febrero = 1.38
c_marzo = 1.14

p_enero = int(input("Ingrese la cantidad producida en enero: "))
p_febrero = int(input("Ingrese la cantidad producida en febrero: "))
p_marzo = int(input("Ingrese la cantidad producida en marzo: "))

ct_enero = (c_enero*p_enero)
ct_febrero = (c_febrero*p_febrero)
ct_marzo = (c_marzo*p_marzo)

print(f"Los costos totales de producción son: ${ct_enero+ct_febrero+ct_marzo:.2f}")

#2) Crear una lista de los 5 días de la semana

días = ["lunes", "martes", "miercoles", "jueves", "viernes"]
productos = [0,0,0,0,0]

lu= int(input())
productos[0] = lu
ma= int(input())
productos[1] = ma
mi= int(input())
productos[2] = mi
ju= int(input())
productos[3] = ju
vi= int(input())
productos[4] = vi

print(f"El día {días[0].upper()} se vendieron {productos[0]} productos")
print(f"El día {días[1].upper()} se vendieron {productos[1]} productos")
print(f"El día {días[2].upper()} se vendieron {productos[2]} productos")
print(f"El día {días[3].upper()} se vendieron {productos[3]} productos")
print(f"El día {días[4].upper()} se vendieron {productos[4]} productos")

print(f"Se vendieron un total de {sum(productos)}")"""

#3) Fruta favorita de niños

frutas = [1,2,3,4,5,6]

niño1 = int(input())
fruta1 = input()
frutas[niño1] = fruta1

print(frutas)

niño2 = int(input())
fruta2 = input()
frutas[niño2] = fruta2

print(frutas)

niño3 = int(input())
fruta3 = input()
frutas[niño3] = fruta3

print(frutas)

niño4 = int(input())
fruta4 = input()
frutas[niño4] = fruta4

print(frutas)

niño5 = int(input())
fruta5 = input()
frutas[niño5] = fruta5

print(frutas)

niño6 = int(input())
fruta6 = input()
frutas[niño6] = fruta6

print(frutas)




#4)Yo trabajo para la empresa, se le pide que consturya dos propuestas de correo. Si la persona escribe más de una mayúscula, todo debe ser minúscula}

nombre = input("nombre: ")
apellido = input("apellido: ")

print(f"{nombre.lower()}.{apellido.lower()}@ISND.com")
print(f"{nombre.lower()[0]}{apellido.lower()}@ISND.com")

#5) Verificar si tiene signo de dolar

salario = input("Ingrese su salario: ")

print(salario[0] == "$")
print(salario.count("$")==1)