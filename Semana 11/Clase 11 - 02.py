#def describir_mascota(tipo_animal: str="perro", nombre_mascota: str=""):
 #   """Esta función describe una mascota, por defecto = perro"""
  #  print(f"Mi mascota es un {tipo_animal} y se llama {nombre_mascota.capitalize()}")
#describir_mascota(nombre_mascota="jaime",)
#describir_mascota("","misifus")
#describir_mascota("","pepe")
#def registro_usuarios(nombre, apellido, inicial = "", edad = 0):
 #   """Construir un nombre a partir de sus componentes"""
  #  if edad:
   #     texto_completo = f"La persona se llama {nombre} {inicial} {apellido} y tiene {edad} años de edad"
    #else:
     #   texto_completo = f"La persona se llama {nombre} {inicial} {apellido}"
    
    #return texto_completo
#print(registro_usuarios("Daniel", "Wisecarver"))
def saludar_usuarios(nombre):
    """Saludará usuario"""
    print(f"Holi, {nombre}. Que gusto verte.")
usuarios = ["Ana", "Luis", "Juan"]
for n in usuarios:
    saludar_usuarios(n)

def ordenar_pizza(size, masa, *ingredientes): #ahora con args
    """Vamos a imprimir su orden"""
    print(f"Usted ha ordenado una pizza {size} de {masa} con:")
    for i in ingredientes:
        print(f"- {i.capitalize()}")
ordenar_pizza(input("¿Que tamaño la quiere?: "), input("¿Que masa?: "),"queso", "cochino", "JamoncitTO0", "piña", "mango")    