palabra = input()

alreves = palabra.lower()[::-1]
palindromo = palabra.lower() == alreves

print(palindromo)