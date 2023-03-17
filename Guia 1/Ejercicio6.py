def contar_vocales(frase):
    
    contador = 0
    
    for letra in frase:

        if letra in "aeiou":
            contador += 1
    
    print("El contador es:", contador)
    
    return contador


contar_vocales("agustin")