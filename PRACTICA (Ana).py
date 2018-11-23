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
  numero_3= numero_4
if(numero_1 > numero_2 > numero_3):
  numero_4 = numero_1
  numero_1 = numero_3
  numero_3 = numero_4
if(numero_1 > numero_2 < numero_3):
  numero_4 = numero_2
  numero_1 = numero_2
  numero_1 = numero_4
if((numero_1 == numero_2) > numero_3):
  numero_4 = numero_3
  numero_3 = numero_1
  numero_1 = numero_4
if(numero_2 < (numero_1 == numero_3)):
  numro_4 = numero_2
  numero_2 = numero_1
  numero_1 = numero_4
if(numero_1 > (numero_2 == numero_3)):
  numero_4 = numero_3
  numero_3 = numero_1
  numero_1 = numero_4
print(numero_1, numero_2, numero_3)


#coding: utf-8
#Versio 1.1
#Joc de proves
n_1 = int(input("Escriu un nombre:"))
n_2 = int(input("Escriu un altre nombre:"))
if(n_1 > n_2):
  print(n_1)
if(n_1 = n_2):
  print("Els nombres son iguals")
else:
  print(n_2)

#coding: utf-8
#Versio 1.1
#Joc de proves
n_1 = int(input("Escriu un nombre:"))
n_2 = int(input("Escriu un altre nombre:"))
n_3 = int(input("Escriu un altre nombre:"))
if(n_1 > n_2 > n_3):
  print(n_1)
if(n_1 = n_2 = n_3):
  print("Els nombres son iguals")
if():
else:
  print(n_2)

#SWAP_1
mano_der = ("mobil")
mano_iz = ("bocadillo")
mano_extra = ()
if(mano_der == "mobil") and (mano_iz == "bocadillo"):
    mano_extra = mano_der
    mano_der = mano_iz
    mano_iz = mano_extra
    print("Mano derecha",mano_der,)
    print("Mano izquierda",mano_iz,)
 
#SWAP_2
cajon1 = ("mobil")
cajon2 = ("bocadillo")
cajon3 = ("boli")
cajon4 = ("bebida")
cajon5 = ()
if(cajon1 == "mobil") and (cajon2 == "bocadillo") and (cajon3 == "boli") and (cajon4 == "bebida"):
  cajon5 = cajon2
  cajon2 = cajon4
  cajon4 = cajon5
  cajon5 = cajon1
  cajon1 = cajon3
  cajon3 = cajon5
  print("Primer cajon:",cajon1,",segundo cajon:",cajon2,",tercer cajon:",cajon3,",quarto cajon:",cajon4,)
