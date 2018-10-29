edad = int(input("¿Dime tu edad?"))
sexo = input("¿Eres H o M?")
color = int(input("¿Cual es el color de tu pelo? (Rubio, Pelirojo, Moreno)"))
jubilado=input("¿Te has jubilado?")
if ((sexo=="H")and(jubilado=="no")):
    print("Preció: 1€")
if (((sexo=="M")and(color=="Moreno")and(jubilado=="si"))):
   print("Gratis")
if((sexo=="M")and(jubilado=="si")and(color=="Pelirojo")):
   print("Precio: 0.50€")
