correo = input()
pos_arroba = correo.index("@")


tiene_arroba = correo.count("@")==1
tres_c_antes= pos_arroba>=3
tres_c_después= (len(correo) - pos_arroba) >= 3
punto = correo.count(".")>=1
espacios = correo.count(" ")==0
punto_inicio = correo[0] != "."
punto_final = correo[-1] != "."

print(f"{tiene_arroba and tres_c_antes and tres_c_antes and tres_c_después and punto and espacios and punto_inicio and punto_final}")

