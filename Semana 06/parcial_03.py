x = int(input())
A = input()
B = input()

posicionA = int(len(A)//x)
posicionB = int(len(B)//x)

contraseña = A[0:posicionA] + B[-posicionB:]

print(contraseña)

