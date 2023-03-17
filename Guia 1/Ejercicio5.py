def esPalindromo(palabra):

    palabra_al_reves = palabra[::-1]
    
    if palabra == palabra_al_reves:
        return True
    else:
        return False

esPalindromo("tomas")
esPalindromo("neuquen")

