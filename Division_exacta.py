N_1 = int(input("Escribe el dividendo:"))
N_2 = int(input("Escribe divisor:"))
Cociente = (N_1//N_2)
Resto = (N_1%N_2)
if(Cociente == 0):
    print("La división es exacta")
if((Cociente < 0) or (Cociente > 0)):
    print("La división no es exacta, el Cociente es:",Cociente,"y el Resto es:",Resto,)
if(N_2 != 0):
    print("No se puede dividir por 0")
