def contador_numeral(txt):
    """Retorna quantos numeros tem na string"""
    contador = 0
    for elemento in txt:
        if elemento.isdigit():
            contador += 1
    return contador
