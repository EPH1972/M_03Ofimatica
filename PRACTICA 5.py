#coding: utf-8
opcio = input("Que quieres calcular T (triangulo) o C (circulo):")
if(opcio == "C") or (opcio == "c"):
    radi = float(input("Cual es el radio de tu circulo:"))
    print("Tu area es" ,3.14 * radi * 2,)
else:
    if(opcio == "T") or (opcio == "t"):
        base = float(input("Dime la base del triangulo:"))
        altura = float(input("Dime la altura del triangulo:"))
        print("Tu area es",(base*altura) / 2,)
