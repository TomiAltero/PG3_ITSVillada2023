alto = int(input("Alto: "))
ancho = int(input("Ancho: "))
caracter = input("Caracter: ")


for i in range(alto):   
    for j in range(ancho):
        print(caracter, end=" ")
    
    print()
