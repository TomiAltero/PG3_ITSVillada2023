def es_bisiesto(age):
    if(age %4 == 0 and (age %100 != 0 or age %400 == 0)):
        print("El año es biciesto")
    
    else:
        print("El año no es biciesto")


es_bisiesto(2000)
