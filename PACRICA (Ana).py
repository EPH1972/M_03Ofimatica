#coding: utf-8
#Versio 1.1
#Joc de proves
#Entrada:3,-2,0
#Sortida:Positiu,Negatiu,Positiu
numero = int(input("Digues un numero:"))
if(numero >= 0):
  print("El nombre es positiu")
else:
  print("El nombre es negatiu")
  
#coding: utf-8
#Versio 1.1
#Joc de proves
#Entrada:3,-2,0
#Sortida:Positiu,Negatiu,Positiu
#Versio 1.2
#Joc de proves
#Entrada:3,-2,0
#Sortida:Positiu,Negatiu,Neutre
numero = int(input("Digues un numero:"))
if(numero == 0):
  print("El nombre es neutre")
else:
  if(numero > 0):
    print("El nombre es positiu ")
  else:
    print("El nombree es negatiu")

#coding: utf-8
#Versio 1.1
#Joc de proves
#Entrada1:6,12,0
#Entrada2:3,25,0
#Sortida:1 major a 2, 1 menor a 2, els nombres son iguals
numero_1 = int(input("Escriu un numero:"))
numero_2 = int(input("Escriu un altre numero:"))
if(numero_2 < numero_1):
  numero_3 = numero_2
  numero_2 = numero_1
  numero_1 = numero_3
print(numero_1,numero_2)

#coding: utf-8
#Versio 1.1
#Joc de proves
#Entrada1:6,12,0
#Entrada2:3,25,0
#Sortida:1 major a 2, 1 menor a 2, els nombres son iguals
numero_1 = int(input("Escriu un numero:"))
numero_2 = int(input("Escriu un altre numero:"))
numero_3 = int(input("Escriu un altre numero:"))
if(numero_1 < numero_2 > numero_3):
  numero_4 = numero_2
  numero_2 = numero_3
  numero_3 = numero_2
if(numero_1 > numero_2 > numero_3):
  numero_4 = numero_1
  numero_1 = numero_3
  numero_3 = numero_4
if(numero_1 > numero_2 < numero_3):
  numero
print(numero_1, numero_2, numero_3)
