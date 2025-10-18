palabra = input()
letra = input()

ultima_letra = palabra.lower()[-1::] == letra.lower()
print(ultima_letra)