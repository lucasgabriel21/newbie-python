# Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas.

str1 = input()
str2 = input()
str3 = ''

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            if str3.find(str1[i]) == -1:
               str3 = str3 + str1[i]

print(str3)