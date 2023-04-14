def ejercicio_3():
    try:
        meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")


        numero_mes = int(input("Ingresa el número de mes (1-12): "))

        indice = meses[numero_mes - 1]
        print(indice)
    except IndexError:
        print(f"Ingrese un mes valido (1-12) {indice}")

ejercicio_3()
        
