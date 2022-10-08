# Leia uma string. Imprima a string lida com o primeiro caractere em
# maiúsculo, o segundo em minúsculo, o terceiro em maiúsculo, o
# quarto em minúsculo, e assim sucessivamente até o final da string

string = input()

for indice in range(len(string)):
    letra = string[indice]

    if indice % 2 == 0:
        string = string.replace(letra, letra.upper())
    else:
        string = string.replace(letra, letra.lower())

print(string)