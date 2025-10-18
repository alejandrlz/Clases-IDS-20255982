correo = input()

print(f"Contiene exactamente un @: {correo.count('@')== 1}")
print(f"El @ no está ubicado al inicio del correo: {not correo[0].count('@')==1}")
print(f"El @ no está ubicado al final del correo: {not correo[-1].count('@')==1}")