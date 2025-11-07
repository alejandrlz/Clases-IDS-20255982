usuarios = ["Ana", "Carlo", "Luis","Lorenzo", "Pedro"]
edades = [20, 19, 21, 22, 15]
frutas = ["mango", "fresa", "pera", "sandia", "manzana"]

for usuario, edad, fruta in zip(usuarios, edades, frutas): #enumerate separa los valores de lista entre su numero y
    #el valor de su lista
    print(f"El usuario {usuario}, con edad {edad}, le gusta {fruta}")