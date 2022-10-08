#Escreva um programa que leia duas strings e gere uma terceira com os caracteres que aparecem em apenas uma delas.

str1 = input()
str2 = input()
str3 = ''

for i in range(len(str1)):
    if str2.find(str1[i]) == -1:
        if str3.find(str1[i]) == -1:
            str3 = str3 + str1[i]

for j in range(len(str2)):
    if str1.find(str2[j]) == -1:
        if str3.find(str2[j]) == -1:
            str3 = str3 + str2[j]

print(str3)