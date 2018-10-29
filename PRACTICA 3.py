edad = int(input("¿Dime tu edad?"))
sexe = input("¿Eres H o M?")
color = int(input("¿Cual es el color de tu pelo? (Rubio, Pelirojo, Moreno)"))
jubilado=input("¿Te has jubilado?")
if ((sexe=="H")and(jubilado=="no")):
    print("Preció: 1€")
if (((sexe=="M")and(color=="Moreno")and(jubilado=="si"))):
   print("Gratis")
if((sexe=="M")and(jubilado=="si")and(color=="Pelirojo")):
   print("Precio: 0.50€")
