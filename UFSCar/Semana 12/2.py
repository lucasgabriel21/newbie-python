def bissexto(ano):
    """Determina se o ano é bissexto ou nao"""
    return (ano%4==0 or ano%400==0 and ano%100!=0) #True ou False
