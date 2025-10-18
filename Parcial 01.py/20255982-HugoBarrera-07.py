dui = (input())

largo = len(dui) == 10
guion = dui[8] == "-"

ultimo_c = dui[-1]
entero = int(ultimo_c)
si_es_entero = type(entero) == int

print(largo and guion and si_es_entero)
