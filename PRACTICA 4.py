Anyo_actual = int(input("En que año estamos:"))
Anyo_cualquiera = int(input("Dime un año cualquiera:"))
if(Anyo_actual == 0) or (Anyo_cualquiera == 0):
    print("El año 0 no existe")
else:
       if (Anyo_actual == Anyo_cualquiera):
           print("Son el mismo año!")
       if(Anyo_actual > Anyo_cualquiera):
           print("Desde el año",Anyo_cualquiera,"han pasado",Anyo_actual - Anyo_cualquiera - 1,"año/años")
       if(Anyo_actual < Anyo_cualquiera):
           print("Para llegar al año",Anyo_actual,"faltan",Anyo_cualquiera - Anyo_actual - 1,"año/años")
       else:
           print("Esa es la difernacia entre el año",Anyo_actual,"y el año",Anyo_cualquiera,)
