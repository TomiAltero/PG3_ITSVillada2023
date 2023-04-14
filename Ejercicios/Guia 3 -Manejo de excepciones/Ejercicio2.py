def ejercicio2():
    while True:
        try:
            num1 = int(input("Ingrese el numero 1: "))
            num2 = int(input("Ingrese el numero 2: "))

            division = num1 / num2
            print(division)
            break
        except ZeroDivisionError:
            print("Un numero no se puede dividir por 0")
            print("-"*50)
            continue

ejercicio2()