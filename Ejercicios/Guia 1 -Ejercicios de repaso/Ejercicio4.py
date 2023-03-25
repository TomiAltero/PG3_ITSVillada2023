def ordenar_mayor_menor(lista):
    lista.sort(reverse = True)
    return lista

lista = [2 , 8 , 11 , 3 , 56]

print(ordenar_mayor_menor(lista))

"""Usando ordenamiento burbuja tambien se puede hacer"""

array = [5 , 2 , 1 , 55 , 89]
band = False

while band == False:
    band = True
    for i in range(len(array)-1):
        if array[i] > array[i + 1]:
            aux = array[i]
            array[i] = array[i+1]
            array[i+1] = aux
            band = False
print(array)

