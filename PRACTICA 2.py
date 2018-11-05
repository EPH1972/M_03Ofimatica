edad= int(input("Cual es tu edad:"))
if (edad < 5) or (edad >= 65):
  print ("Gratis")
else:
  print ("Pagas 2.15")

  

edad = int(input("¿Dime tu edad?"))
sexo = input("¿Eres H o M?")
color = input("¿Cual es el color de tu pelo?"))
jubilado=input("¿Te has jubilado?")
if ((sexo=="H")and(jubilado=="no")):
    print("Preció: 1€")
if (((sexo=="M")and(color=="Moreno")and(jubilado=="no") or (jubilado=="si") and (edad >= 65) )):
  print("Gratis")
if((sexo=="M")and(jubilado=="si")and(color=="Pelirojo")):
  print("Precio: 0.50€")
else:
  print ("Preció: 1€")
