def ejercicio_4():
    while True:
        try:
            num1 = int(input("Ingrese el numero 1:"))
            num2 = int(input("Ingrese el numero 2:"))
            division = num1 / num2
            print(division)

            while True:
                entrada = input("Desea seguir haciendo calculos (si-no): ")

                if entrada == "si":
                    if entrada.isupper() or entrada.islower():
                        break
                    break
                elif entrada == "no":
                    return
                else:
                    print("Ingrese si o no")
                    continue
        except ValueError:
            print("Ingrese un numero POR FAVOR")
            print("-"*50)
            continue
        except ZeroDivisionError:
            print("No se pude dividir po 0")
            print("-"*50)
            continue
ejercicio_4()   