
def generar_codigo(x,y): 
    numero = int(y) + 1 
    if numero < 10: 
        return(x + "00" + str(numero)) 
    elif numero < 100: 
        return(x + "0" + str(numero)) 
    else: 
        return(x + str(numero))

