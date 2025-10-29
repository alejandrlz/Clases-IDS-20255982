"""#a Positivo o Negativo
numero = int(input())

if numero < 0:
    print("Negativo")
else:
    print("Positivo")"""

#b Anterior y posterior

"""s = int(input())

if s % 2 == 0:
    print(s+2)
    print(s-1)
else:
    print(s+1)
    print(s-2)"""

#c promedio

"""nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())
nota5 = float(input())
nota6 = float(input())

promedio = (nota1+nota2+nota3+nota4+nota5+nota6)/6

if promedio > 9.5:
    print("Gana Premio :)")
else:
    print("No Gana Premio :(")"""

#d Escoger Números 7 y 5

"""ingresados = int(input())

lista = []

for i in range(0,ingresados):
    lista.append(int(input()))

cantidad_sietes = lista.count(7)
cantidad_cincos = lista.count(5)

print(f"{cantidad_sietes} {cantidad_cincos}")"""

#e Los combos de David

n_combos = int(input())

dañoA, dañoB, dañoC = input().split()
dañoA = int(dañoA)
dañoB = int(dañoB)
dañoC = int(dañoC)
combos= []

for n in range(n_combos):
    combos.append(input())


for n in combos:
    A = n.count("A")*dañoA
    B = n.count("B")*dañoB
    C = n.count("C")*dañoC
    print(A+B+C)

#f bodoque enamorado

"""N = int(input())
nombres = []

for n in range(N):
    nombre = input()
    nombres.append(nombre)

for n in nombres:
    letras = len(n)    
    if letras <=6:
        print("No vale la pena")
    elif letras >= 8 :
        print("Si aguanto otro desarrollo de personaje")
    elif letras == 7:
        print("Dios no creo aguantar esta vez")"""

#g mayor que

"""x, y = input().split()
x = int(x)
y = int(y)
print(max(x, y))"""

#h entrada al cine

"""en_fila = int(input())
edades = []
entran = []

for n in range(en_fila):
    edades.append(int(input()))

for n in edades:
    if n >= 15:
        entran.append(1)
    else:
        0

total = sum(entran)   

print(total)"""

#i Ola Ivan

"""estado = input()

if estado == "conectado":
    print("Ola Ivan")
else:
    print("Ol..")"""

#j traficando software

n = int(input())
p=[]
for n in range(n):
    p.append(int(input()))

for n in p:
    if n >=3:
        print("Ok")
    else:
        print("No")