# CONTROL 2 - IDS (Sección 1 y 2)

# Reglas generales:
#   - NO se penaliza usar input("...") como prompt. // Solo para los archivos subidos en Moodle
#   - SÍ se penaliza si la SALIDA (output) no coincide EXACTAMENTE
#     con el formato especificado (texto, orden, espacios, mayúsculas, saltos,
#     True/False, representación de lista, número fijo de decimales, etc.).

#   - Si el envío en OmegaUp obtuvo 100 % en un problema: PUNTAJE COMPLETO.


# ---------------------------------------------------------------
# A) La cena de Alvin – Parte 1  (10 pts)
# Objetivo: Leer un entero n (1..10). Tener una tupla con 10 platos (en orden).
# Imprimir EXACTAMENTE:
#   El plato seleccionado por Alvin es: <nombre>
#
# Desglose de puntaje (10):
#   [5 pts] Estructura correcta: tupla con 10 platos y en el orden esperado.
#   [3 pts] Conversión y ajuste de índice (n-1) para indexar desde 0.
#   [2 pts] Salida EXACTA (mensaje y formato, una sola línea; sin textos extra).
#
# ---------------------------------------------------------------

num_plato = int(input())
tupla_platos = (
    "Hamburguesa",
    "Hotdog",
    "Pizza",
    "Tacos",
    "Lasaña",
    "Ensalada",
    "Pupusas",
    "Burrito",
    "Alitas de pollo",
    "Papas fritas",
)
# Ajuste de índice (n-1). Se asume input válido 1..10 según enunciado:
plato = tupla_platos[num_plato - 1]
print(f"El plato seleccionado por Alvin es: {plato}")


# ---------------------------------------------------------------
# B) La cena de Alvin – Parte 2  (20 pts)
# Objetivo: Lista con 10 precios. Leer:
#   - número de plato a corregir (1..10)
#   - nuevo precio (float)

# Actualizar el precio en la posición correspondiente e imprimir EXACTAMENTE:
#   Los precios actualizados son: [lista]
# (Usar la representación estándar de Python de la lista)
#
# Desglose de puntaje (20):
#   [7 pts] Lista base con 10 precios correctos y en el orden esperado.
#   [3 pts] Lecturas correctas: plato (int) y nuevo precio (float).
#   [6 pts] Actualización en la posición correcta (ajuste de índice).
#   [4 pts] Salida EXACTA: texto + lista completa en una sola línea, sin extras.
#
# ---------------------------------------------------------------

pos_plato = int(input())
nuevo_precio_1 = float(input())

lista_precios = [3.52, 55.15, 4.25, 60.25, 5.65, 3.15, 2.65, 70.75, 6.25, 2.55]

lista_precios[pos_plato - 1] = nuevo_precio_1

print(f"Los precios actualizados son: {lista_precios}")


# ---------------------------------------------------------------
# C) Los correos de la ESEN  (20 pts)
# Objetivo: Leer string 'correo' y verificar/imprimir 3 líneas EXACTAS:
#   1) Contiene exactamente un @: True/False
#   2) El @ no está ubicado al inicio del correo: True/False
#   3) El @ no está ubicado al final del correo: True/False
#
# Desglose de puntaje (20):
#   [6 pts] Conteo de '@' == 1.
#   [5 pts] Verificación de no inicio (correo[0] != '@')*.
#   [5 pts] Verificación de no final (correo[-1] != '@')*.
#   [4 pts] Formato EXACTO de las 3 líneas (texto, orden, True/False).
#
# ---------------------------------------------------------------

correo = input()

cantidad_arrobas = correo.count("@")
cantidad_valida = (cantidad_arrobas == 1)

arroba_no_inicio = (correo[0] != "@")
arroba_no_final = (correo[-1] != "@")

print(f"Contiene exactamente un @: {cantidad_valida}")
print(f"El @ no está ubicado al inicio del correo: {arroba_no_inicio}")
print(f"El @ no está ubicado al final del correo: {arroba_no_final}")


# ---------------------------------------------------------------
# D) ¡LAS NOTAS!  (20 pts)
# Objetivo: Leer 5 decimales (en orden): C1, P1, C2, P2, Tarea.
# Calcular promedio ponderado con pesos:
#   C1 15 %, P1 40 %, C2 25 %, P2 20 %, Tarea 5 %
# Imprimir EXACTAMENTE:
#   La nota final es: XX.XX
# con 2 decimales fijos (:.2f).
#
# Desglose de puntaje (20):
#   [5 pts] Lectura de 5 entradas en el orden C1, P1, C2, P2, Tarea.
#   [6 pts] Pesos correctos (0.15, 0.40, 0.25, 0.20, 0.05).
#   [5 pts] Cálculo correcto del ponderado.
#   [4 pts] Salida EXACTA con 2 decimales fijos. 
#
# ---------------------------------------------------------------

c1 = float(input())
p1 = float(input())
c2 = float(input())
p2 = float(input())
tarea = float(input())

nota_final = (c1 * 0.15) + (p1 * 0.40) + (c2 * 0.25) + (p2 * 0.20) + (tarea * 0.05)

print(f"La nota final es: {nota_final:.2f}")


# ---------------------------------------------------------------
# E) La Contraseña de Alvin  (30 pts)
# Objetivo: Leer M (int), S (int), A (str), B (str)
#   - primera parte = A[::S]
#   - segunda parte = "_Alvin"
#   - tercera parte = B repetida M veces
# Salida: una única línea con la concatenación EXACTA, sin espacios extra.
#
# Desglose de puntaje (30):
#   [4 pts] Lecturas y tipos correctos (int, int, str, str).
#   [8 pts] Slicing correcto A[::S] 
#   [6 pts] Repetición exacta B * M.
#   [8 pts] Concatenación exacta, sin espacios/sep extra.
#   [4 pts] Salida en una sola línea, sin texto adicional.
#
# ---------------------------------------------------------------

m = int(input())
s = int(input())
a = str(input())
b = str(input())

texto_con_saltos = a[::s]
texto_final = texto_con_saltos + "_Alvin" + (b * m)
print(texto_final)