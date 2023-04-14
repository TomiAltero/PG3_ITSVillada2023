def ejercicio_5():

    try:
        while True:
            with open("PG3_ITSVillada2023/Ejercicios/Guia 3 -Manejo de excepciones/archivo.txt", "w") as archivo:
                dicc = {"Nombre": "Tomas", "Apellido":"Altero", "Edad": 17}
                numero = 17
                for c,v in dicc.items():
                    archivo.write(c + ":" + str(v) +"\n")
                archivo.write(numero)
    except TypeError:
        print("No se puede ingresar un valor numerico, debes convertirlo a str")
ejercicio_5()