#coding: utf-8
opcio = input("Que vols calcular T (triangle) o C (cercle):")
if(opcio == "C") or (opcio == "c"):
    radi = float(input("Quin es el radi del teu cercle:"))
    print("La teva area es" ,3.14 * radi * 2,)
else:
    if(opcio == "T") or (opcio == "t"):
        base = float(input("Digues la base del triangle:"))
        altura = float(input("Digues l'alsada del triangle:"))
        print("La teva area es",(base*altura) / 2,)
