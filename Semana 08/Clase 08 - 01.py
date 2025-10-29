numeros = [1,2,3,4]
palabra = "Aulas"
dias = ["lunes", "martes", "miercoles", "jueves", "viernes",
"sábado", "domingo"]
#print(len(palabra))

"""for x in dias:
    print(x[:2])"""

"""for i in (range(0,10,2)): #igual que los corchetes
    
    print(i) #incluye el primero y el ultimo no

personas = ["Ana", "Luis", "Luisa"]
for p in personas:
    print(p)
    for l in p:
        print(l)"""

valores = [[1,3,6], [2,7,4], [6,5,4], [1,10,20]]
mayores = []
for v in valores:
    for i in v:
        if i > 6:
            mayores.append(i)

print(mayores)


presupuesto = 1000
gasto = 0
while gasto <= presupuesto:
    compra = float(input("Digite el valor de compra: "))
    gasto += compra
gasto -=compra
print(gasto)

estado = "Conectado"
while estado == "Conectado":
    print("Hola Sebas")
    estado = input("Digite su estado: ")
