def ejercicio1():

    while True:
        try:
            num1 = int(input("Ingrese el numero 1: "))
            num2 = int(input("Ingrese el numero 2: "))
        
            suma = num1 + num2

            print(suma)
            break
        except ValueError:
            print("Ingrese un numero, no una letra o una palabra")
            print("-"*50)
            continue

ejercicio1()