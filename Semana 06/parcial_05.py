a= float(input())
b= float(input())
c= float(input())
d= float(input())
e=float(input())
f = float (input())

datos = [a,b,c,d,e,f]

resta = max(datos)-min(datos)

print(f"Maximo: {max(datos):.2f}")

print(f"Minimo: {min(datos):.2f}")

print(f"Diferencia: {resta:.2f}")
print(f"Suma: {sum(datos):.2f}")
print(f"Promedio: {sum(datos)/6:.2f}")