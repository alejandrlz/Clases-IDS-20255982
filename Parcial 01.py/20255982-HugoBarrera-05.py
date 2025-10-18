palabra = input()
letra = input()

contiene = palabra.lower().count(letra.lower())

si_tiene = contiene > 0

print(si_tiene)