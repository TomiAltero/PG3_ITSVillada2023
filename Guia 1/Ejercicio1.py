def buscar_indice(lista, elemento):
    indice = -1
    for i in range(len(lista)):
        if lista[i] == elemento:
            indice = i
            break
    return indice

lista = [8, 12, 9, 45]

while True:
    elemento = int(input("Ingrese el valor a buscar en la lista (ingrese 'q' para salir): "))

    indice = buscar_indice(lista, elemento)

    if indice != -1:
        print(f"El elemento {elemento} se encuentra en la posición {indice} de la lista {lista}")
    else:
        print(f"El elemento {elemento} no se encuentra en la lista {lista}, el indice es {indice}")
